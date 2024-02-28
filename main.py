# NLP processing
import os
import pgf
import process

# location events
import lake

# other assisting
import helper
import time

inventory = [None] * 10 # create empty inventory of 10 items

def main():
    os.system("gf -make AdventureEng.gf") # generate PGF file
    gr = pgf.readPGF("Adventure.pgf") # read PGF file
    lang = gr.languages["AdventureEng"] # get English languge (default)
    
    quit = False
    success = False
    loc = [0,0] # starting location

    while not quit:
        try:
            args = process.get_input(lang)
        except:
            exit()

main()