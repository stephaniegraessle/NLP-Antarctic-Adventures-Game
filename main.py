# NLP processing
import os
import pgf
import process
import helper

# location events
import lake

# other assisting
import helper
import time

def main():
    os.system("gf -make AdventureEng.gf") # generate PGF file
    gr = pgf.readPGF("Adventure.pgf") # read PGF file
    lang = gr.languages["AdventureEng"] # get English languge (default)
    #process.print_grammar_info(gr) # Print info about grammar

    environ = helper.gen_environ() # intialize starting environment

    loc = [0,0] # initialize starting location
    inventory = [None] * 10 # create empty inventory of 10 items--change to [None,0]?
    hunger = 100 # initialize full hunger
    hp = 100 # initialize full hp

    quit = False
    success = False
    while not quit:
        try:
            

            # program gives information about environment

            args = process.get_input(lang) # get user input

            # determine which type of command the user inputted

            # determine useful information from command, e.g., verb, determiners, objects, etc.

            # do appropriate followup action


            # determiner function testing
            #det = process.get_det(args,gr)
            #print("Det:",det)
            #det_amt = process.get_det_amount(det)
            #print("Det amount:",det_amt)

        except:
            #os.system("rm Adventure.pgf") # remove generated PGF file
            exit()

main()
