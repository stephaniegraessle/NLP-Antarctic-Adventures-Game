# NLP processing
import os
import pgf
import process
import helper

# constants
import constant

# other assisting
import helper
import output
import event

def main():
    os.system("gf -make AdventureEng.gf") # generate PGF file
    gr = pgf.readPGF("Adventure.pgf") # read PGF file
    lang = gr.languages["AdventureEng"] # get English languge (default)
    #process.print_grammar_info(gr) # Print info about grammar

    output.welcome(lang)

    loc = (0,0) # init starting location
    output.loc(loc,lang)
    environ, ground = helper.gen_environ(loc,lang) # give information about and describe environment

    #map = {} # init map dictionary containing all location info
    #map.update({loc:info}) # add starting location and environment/item info to map

    inv = {} # init empty dictionary as inventory

    hunger = constant.MAX_HUNGER # init full hunger
    hp = constant.MAX_HP # init full hp

    quit = False
    dead = False
    while not dead and not quit: # TODO: Make 'quit' functional
        #print()
        try:
            output.see(ground,lang)
            output.status(hunger,hp,lang)
            output.inventory(inv,lang)

            func,args = process.get_input(lang) # get user input as func, args

            action = process.determine_action(func) # determine what the user inputted
            #print("Action:\t",action)

            # TODO: Put this into a separate process.py function
            if action == 'navigation':
                loc = process.execute_navigation(loc,args,lang,gr) # move to new loc
                environ, ground = helper.gen_environ(loc,lang) # generate new environment
            elif action == 'command':
                ground,inv,hunger,hp,quit = process.execute_command(environ,ground,inv,hunger,hp,args,lang,gr)

            hunger = helper.lose_hunger(hunger,constant.NORMAL_HUNGER_LOSS_RATE) # lose hunger per turn
            #TODO: Make it such that not lose hunger if eating that turn
            hp = helper.check_if_starving(hunger,hp) # lose HP if hunger too low
            dead = helper.check_if_dead(hp,lang)
        except:
            output.log("main.py main()","function failed")
            #os.system("rm Adventure.pgf") # remove generated PGF file
            event.quit(lang)
main()
