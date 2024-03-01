import pgf

PUNCT = ['.','!','?',',',':',';']

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
# input: PGF expression
# output: string
def linearize(expr, lang):
    expr = pgf.readExpr(expr)
    expr = lang.linearize(expr)
    return expr

# Outputs "The input is invalid."
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
            sent = input("Enter sentence: ")
            sent = preprocess(sent) # preprocess sentence

            i = lang.parse(sent) # parse sentence
            p,e = i.__next__() # get iterator, function and arguments from parse
            func, args = e.unpack()

            test(func,args) # print parsed results

            success = True
        except:
            invalid(lang)
    return args