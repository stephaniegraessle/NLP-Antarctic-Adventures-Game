# NLP processing
import os
import pgf
import process
import helper

# constants
import constant

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

    environ = helper.gen_environ() # init starting environment

    loc = [0,0] # init starting location
    inv = {} # init empty dictionary as inventory
    hunger = constant.MAX_HUNGER # init full hunger
    hp = constant.MAX_HP # init full hp

    quit = False
    success = False
    while not quit and hp > 0: # TODO: Make dialogue for if die from low HP
        print()
        try:
            helper.print_stats(hunger,hp)
            helper.print_inv(inv)

            # program gives information about environment

            input = process.get_input(lang) # get user input as list of [func,args]
            func = input[0]
            args = input[1]

            # determine which type of command the user inputted
            #type = process.get_type(args)

            # determine useful information from command, e.g., verb, determiners, objects, etc.

            # do appropriate followup action


            # determiner function testing
            #det = process.get_det(args,gr)
            #print("Det:",det)
            #det_amt = process.get_det_amount(det)
            #print("Det amount:",det_amt)

            hunger = helper.lose_hunger(hunger,constant.NORMAL_HUNGER_LOSS_RATE) # lose hunger per turn
            hp = helper.check_if_starving(hunger,hp) # lose HP if hunger too low
        except:
            #os.system("rm Adventure.pgf") # remove generated PGF file
            exit()

main()
