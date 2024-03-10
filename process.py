import pgf
import helper
import constant
import event
import output
import random

PUNCT = ['.','!','?',',',':',';']

def print_grammar_info(gr):
    categories = gr.categories
    print("\nAll categories:\n",categories)
    
    for c in categories:
        print("\nFunctions in",c,"category:\n",gr.functionsByCat(c))
    
    #print("\nAll functions:\n",gr.functions)
    print("\nFunction type of 'a_Det':\n",gr.functionType("a_Det"))
    print("\nFunction type Python type:\n",type(gr.functionType("a_Det")))

# Preprocesses user input for prepare it for parsing.
# Input: string
# Output: string
def preprocess(sent):
    try:
        sent = sent.lower() # all to lowercase
        # TODO: make exception for "I"... once done fix grammar files
        for i in PUNCT: # remove punctuation
            sent = sent.replace(i,'')
    except:
        output.log("process.py preprocess()","failed")
    return sent

# Postprocesses generated expressions which are to be printed.
# Input: string
# Output: string
def postprocess(sent, punct):
    try:
        sent = sent.capitalize() # capitalize first letter of sentence
        sent = sent + punct # add on correct punctuation
    except:
        output.log("process.py postprocess()","failed")
    return sent

# Reads a PGF expression and linearizes it to a string.
# Input: PGF expression
# Output: string
def linearize(expr, lang):
    try:
        expr = pgf.readExpr(expr)
        expr = lang.linearize(expr)
    except:
        output.log("process.py linearize()","failed")
    return expr

# Input: Statement to say, language which statement should be linearized to (e.g., 'Invalid')
# Output: Linearized and postprocessed print statement
def PGF_to_string(expr,punct,lang):
    try:
        output = linearize(expr, lang)
        output = postprocess(output,punct)
        return output
    except:
        output.log("process.py PGF_to_string()","failed")

def print_parse(func, args):
    for i in range(2):
        try:
            if i == 0:
                print("\tFunc:\t", func)
            elif i == 1:
                print("\tArgs:\t", args)
        except:
            print("\tTest error.")
    
    print("\tArgs:")
    for a in args:
        try:
            print("\t",a)
        except:
            print("\tTest error.")

def get_input(lang):
    success = False
    while not success:
        try:
            sent = input("\nEnter input: ") # TODO: change to linearized grammar statement
            print()
            sent = preprocess(sent) # preprocess sentence

            i = lang.parse(sent) # parse sentence
            p,e = i.__next__() # get iterator, function and arguments from parse
            func, args = e.unpack()

            #print_parse(func,args) # print parsed results

            success = True
            msg = "successful parse - \'" + sent + "\'"
            output.log("process.py get_input()",msg)
        except:
            # TODO: make separate function for logging
            # log unparsable sentences

            log = open("parse_errors.log",'a') # open log file in append mode
            log.write(sent) # append sentence that could not be parsed
            log.write('\n')
            log.close()
            
            output.log("process.py get_input()","failed")
            msg = "parse error - \'" + sent + "\'"
            output.log("process.py get_input()",msg)
            output.error(constant.INVALID_INPUT_EXPR,lang) # print error message
    return [func,args]

# Determine which action to take based on the function of the parsed user input
# Input: function PGF expression, list of PGF expressions
# Output: True if found a function, False if did not find a match
def determine_action(func):
    try:
        if func in constant.COMMAND_FUNCS:
            return 'command'
        elif func in constant.NAVIGATION_FUNCS:
            return 'navigation'
        return 'None' # did not find a way to process the user input
    except:
        output.log("process.py determine_action()","failed")

# Determine which type of command to carry out
# Output: modified ground, inv, hunger, hp values
def execute_command(environ,ground,inv,hunger,hp,args,lang,gr):
    v = get_word_by_func('V',args,gr)
    v2 = get_word_by_func('V2',args,gr)
    det = get_word_by_func('Det',args,gr)
    obj = get_word_by_func('Feat',args,gr)

    det_amt = get_det_amount(det)

    quit = False

    if v2 in constant.DROP_WORDS: # drop item
        ground,inv = event.drop(ground,inv,det_amt,obj,lang)
    elif v in constant.EAT_WORDS or v2 in constant.EAT_WORDS: # eat
        inv,hunger,hp = event.eat(ground,inv,hunger,hp,det_amt,obj,lang)
    elif v2 in constant.PICK_UP_WORDS: # pick up item
        ground,inv = event.pick_up(ground,inv,det_amt,obj,lang)
    elif v in constant.HELP_WORDS or v2 in constant.HELP_WORDS:
        event.help(lang)
    elif v in constant.QUIT_WORDS or v2 in constant.QUIT_WORDS:
        event.quit(lang)
        quit = True
    return ground,inv,hunger,hp,quit
            
def execute_navigation(loc,args,lang,gr):
    try:
        dir = get_word_by_func('Dir',args,gr) # get direction word from args
        loc = helper.move(loc,dir) # move to new location
        output.move_loc(loc,lang)
    except:
        output.log("process.py execute_navigation()","failed")
    return loc

# Input: list of PGF expressions, grammar
# Output: detemerminer of sentence as string
def get_det(args,gr):
    try:
        det_list = gr.functionsByCat("Det") # list of all determiners in grammar
        
        for a in args: # go thru words in sentence
            for d in det_list: # go thru determiners in grammar
                if a == pgf.readExpr(d):
                    return d # return determiner as string
    except:
        output.log("process.py get_det()","failed")
    return "None" # No determiner found in sentence

# Returns first found word that matches the indicated word type
# Input: part of sentence/word type string (e.g., "Det"), list of PGF expressions, grammar
# Output: String word found in grammar or "None" if none of that type found
def get_word_by_func(part,args,gr):
    word_list = gr.functionsByCat(part) # list of all determiners in grammar
    
    for a in args: # go thru words in sentence
        for word in word_list: # go thru determiners in grammar
            if a == pgf.readExpr(word):
                return word # return determiner as string
    return 'None' # No determiner found in sentence

# Input: det in PGF expression
# Output: determiner amount as integer (e.g., a,the,1, etc.=1; 2,two=2, etc.)
def get_det_amount(det):
    try:
        count = 0
        for num in constant.NUMS:
            for word in num:
                if det == word:
                    return count # return corresponding number of objects with determiner
            count+=1
    except:
        output.log("process.py get_det_amount()","failed")
    return 0 # no match

# enter a number, returns a determiner from constants coinciding with amount given
def get_det_from_amount(amt):
    try:
        if amt == 1:
            return 'a_Det'
        else:
            choices = constant.NUMS[amt]
            return random.choice(choices)
    except:
        output.log("process.py get_det_from_amount()","failed")

def feat_to_str(feat,lang):
    expr = 'FeatAlone ' + feat
    str = PGF_to_string(expr,' ',lang)
    return str