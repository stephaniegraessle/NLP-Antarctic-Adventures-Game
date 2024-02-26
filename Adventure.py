import os
import pgf
import event
import helper
import process
import time

inventory = [None] * 10 # create empty inventory of 10 items

def main():
    os.system("gf -make AdventureEng.gf") # generate PGF file
    gr = pgf.readPGF("Adventure.pgf") # read PGF file
    lang = gr.languages["AdventureEng"] # get English languge (default)
    
    quit = False
    success = False

    while not quit:
        try:
            args = process.getinput(lang)
        except:
            exit()

    #     while not success:
    #         try:
    #             sent = input("Enter sentence: ")

    #             sent = process.preprocess(sent)

    #             if sent == 'quit':
    #                 quit = True
    #                 break

    #             i = lang.parse(sent)
    #             p,e = i.__next__() # get iterator, function and arguments from parse

    #             func, args = e.unpack()

    #             process.test(func,args)

    #             success = True
    #             continue
    #         except:
    #             process.invalid(lang)

main()