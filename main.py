# NLP processing
import os
import pgf
import process

# location events
import lake

# other assisting
import helper
import time

def main():
    os.system("gf -make AdventureEng.gf") # generate PGF file
    gr = pgf.readPGF("Adventure.pgf") # read PGF file
    lang = gr.languages["AdventureEng"] # get English languge (default)
    
    loc = [0,0] # initialize starting location
    inventory = [None] * 10 # create empty inventory of 10 items--change to [None,0]?

    quit = False
    success = False
    while not quit:
        try:
            args = process.get_input(lang)
        except:
            #os.system("rm Adventure.pgf") # remove generated PGF file
            exit()

main()
