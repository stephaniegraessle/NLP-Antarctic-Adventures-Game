import pgf

PUNCT = ['.','!','?',',',':',';']

def print_grammar_info(gr):
    print("\nCategories:\n",gr.categories)
    print("\nFunctions:\n",gr.functions)
    print("\nFunction type of 'a_Det':\n",gr.functionType("a_Det"))
    print("\nFunction type Python type:\n",type(gr.functionType("a_Det")))

# Preprocesses user input for prepare it for parsing.
# Input: string
# Output: string
def preprocess(sent):
    sent = sent.lower() # all to lowercase
    # TODO: make exception for "I"... once done fix grammar files
    for i in PUNCT: # remove punctuation
        sent = sent.replace(i,'')
    return sent

# Postprocesses generated expressions which are to be printed.
# Input: string
# Output: string
def postprocess(sent, punct):
    sent = sent.capitalize() # capitalize first letter of sentence
    sent = sent + punct # add on correct punctuation
    return sent

# Reads a PGF expression and linearizes it to a string.
# Input: PGF expression
# Output: string
def linearize(expr, lang):
    expr = pgf.readExpr(expr)
    expr = lang.linearize(expr)
    return expr

# Input: Language which statement should be linearized to
# Output: Print statement for invalid input
def invalid(lang):
    output = linearize("Invalid", lang)
    output = postprocess(output, '.')
    print(output)

def test(func, args):
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
            sent = input("\nEnter sentence: ")
            sent = preprocess(sent) # preprocess sentence

            i = lang.parse(sent) # parse sentence
            p,e = i.__next__() # get iterator, function and arguments from parse
            func, args = e.unpack()

            test(func,args) # print parsed results

            success = True
        except:
            invalid(lang)
    return [func,args]

# Input: list of PGF expressions
# Output: One-word string of which type of sentence the args contains
# Sentences types:
# - Question
# - Navigation
#def get_type(args):

# Input: list of PGF expressions
# Output: verb of sentence as string
#def get_verb(args):

# Input: list of PGF expressions
# Output: detemerminer of sentence as string
def get_det(args,gr):
    det_list = gr.functionsByCat("Det") # list of all determiners in grammar
    
    for a in args: # go thru words in sentence
        for d in det_list: # go thru determiners in grammar
            if a == pgf.readExpr(d):
                return d # return determiner as string
    return "None" # No determiner found in sentence
    # TODO: May need to change this to PGF expr or other form

# Input: det in PGF expression
# Output: determiner amount as integer (e.g., a,the,1, etc.=1; 2,two=2, etc.)
def get_det_amount(det):
    zero = ["no_Det","zero_Det","zero_num_Det"]
    one = ["a_Det","an_Det","a_n_Det", "missingdet_Det","that_Det","the_Det","this_Det","one_Det","one_num_Det"]
    two = ["acouple_Det","two_Det","two_num_Det"]
    three = ["three_Det","three_num_Det"]
    four = ["four_Det","four_num_Det"]
    five = ["five_Det","five_num_Det"]
    six = ["six_Det","six_num_Det"]
    seven = ["seven_Det","seven_num_Det"]
    eight = ["eight_Det","eight_num_Det"]
    nine = ["nine_Det","nine_num_Det"]
    ten = ["ten_Det","ten_num_Det"]

    nums = [zero,one,two,three,four,five,six,seven,eight,nine,ten]
    
    count = 0
    for n in nums:
        for word in n:
            if det == word:
                return count # return corresponding number of objects with determiner
        count+=1

    return -1 # no match


