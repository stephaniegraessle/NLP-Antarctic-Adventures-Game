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

main()