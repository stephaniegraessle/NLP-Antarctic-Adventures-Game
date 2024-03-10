from datetime import datetime as dt
import time
import helper
import process
import constant
# Contains dialogue functions for certain scenarios
# Organize functions alphabetically
# TODO: Add constants for expressions to make easier to modify/add new ones

def parse_error_log(sent):
    log = open("parse_errors.log",'a') # open log file in append mode
    log.write(sent) # append sentence that could not be parsed
    log.write('\n')
    log.close()

def log(type,message):
    type = type + ':'
    date = str(dt.now())
    log = open("event_log.log",'a') # open log file in append mode
    log.write("[" + date + "] ")
    if type != None:
        log.write(type)
        log.write(" ")
    log.write(message)
    log.write('\n')
    log.close()

# Outputs a custom expression in scenarios with specific static expressions
# Works the same as error()
def custom(expr,punct,lang):
    out = process.PGF_to_string(expr,punct,lang)
    print(out)
    time.sleep(constant.DELAY)

def custom_feat(feat,lang):
    expr = 'FeatAlone ' + feat
    out = process.PGF_to_string(expr,' ',lang)
    print(out, end="")
    time.sleep(constant.DELAY)

def dont_have(item,lang):
    log("output.py dont_have()","function called")
    expr = constant.DONT_HAVE_EXPR + ' ' + item
    out = process.PGF_to_string(expr,'.',lang)
    print(out)
    time.sleep(constant.DELAY)

def death(lang):
    log("output.py death()","function called")
    custom(constant.DEATH_EXPR,'.',lang)
    time.sleep(constant.DELAY)

def drop(det_amt,item,lang):
    log("output.py drop()","function called")
    try:
        expr = constant.DROP_EXPR
        det = process.get_det_from_amount(det_amt)
        expr = expr + ' ' + det + ' ' + item
        out = process.PGF_to_string(expr,'.',lang)
        print(out)
        time.sleep(constant.DELAY)
    except:
        log('output.py drop()','did not succeed')

def loc(loc,lang):
    log("output.py loc()","function called")
    expr = constant.CURRENT_LOC_EXPR
    expr = expr
    out = process.PGF_to_string(expr,' ',lang)
    print(out + str(loc))
    time.sleep(constant.DELAY)

def environ(environ,lang):
    log("output.py environ()","function called")
    expr = constant.ENVIRON_EXPR
    if environ == 'ocean_Loc':
        expr = expr + ' the_Det ocean_Loc'
    elif environ == 'snowfield_Loc':
        expr = expr + ' a_Det snowfield_Loc'
    out = process.PGF_to_string(expr,'.',lang)
    print(out)
    time.sleep(constant.DELAY)

# Works same as custom() but specifies that the output is an error message for code readability
def error(error_expr,lang):
    log("output.py error()","function called")
    out = process.PGF_to_string(error_expr,'.',lang)
    print(out)
    time.sleep(constant.DELAY)

def goodbye(lang):
    log("output.py goodbye()","function called")
    custom(constant.GOODBYE_EXPR,'!',lang)
    time.sleep(constant.DELAY)

def ground(ground,lang):
    log("output.py ground()","function called")
    print("ground()")
    time.sleep(constant.DELAY)

def hunger_status(hunger,lang):
    log("output.py hunger_status()","function called")
    expr = constant.HUNGER_EXPR
    out = process.PGF_to_string(expr,':',lang)
    print(out + " " + str(hunger))
    time.sleep(constant.DELAY)

def hp_status(hp,lang):
    log("output.py hp_status()","function called")
    expr = constant.HP_EXPR
    out = process.PGF_to_string(expr,':',lang)
    print(out + " " + str(hp))
    time.sleep(constant.DELAY)

# Prints inventory contents
def inventory(inv,lang):
    log("output.py inventory()","function called")
    try:
        if len(inv) > 0:
            expr = constant.INV_EXPR
            out = process.PGF_to_string(expr,':',lang)
            print(out,end=' ')

            for item in inv.keys():
                feat = process.feat_to_str(item,lang)
                print(feat,end='')
                print('(' + str(inv[item]) + ')',end=' ')
            print()
        else:
            expr = constant.INV_EMPTY_EXPR
            out = process.PGF_to_string(expr,'.',lang)
            print(out)
        time.sleep(constant.DELAY)
    except:
        log('output.py inventory()','did not succeed')

def move_loc(loc,lang):
    log("output.py move_loc()","function called")
    expr = constant.MOVE_LOC_EXPR
    out = process.PGF_to_string(expr,' ',lang)
    out = out + str(loc)
    print(out)
    time.sleep(constant.DELAY)

def pick_up(det_amt,item,lang):
    log("output.py pick_up()","function called")
    try:
        expr = constant.PICK_UP_EXPR
        det = process.get_det_from_amount(det_amt)
        expr = expr + ' ' + det + ' ' + item
        out = process.PGF_to_string(expr,'.',lang)
        print(out)
        time.sleep(constant.DELAY)
    except:
        log('output.py pick_up()','did not succeed')

# Prints the first item from the ground list
def see(ground,lang):
    log("output.py see()","function called")
    try:
        ground_total = len(ground)
        if ground_total > 0:
            item = ground[0] # get first ground item
            det = 'some_Det'
            expr = constant.SEE_EXPR + " " + det + " " + item
    except:
        expr = constant.SEE_NOTHING_EXPR
    out = process.PGF_to_string(expr,'.',lang)
    print(out)
    # TODO: Expression for can't see anything
    time.sleep(constant.DELAY)

# Gives hunger and hp status
# "How am I?"
def status(hunger,hp,lang):
    log("output.py status()","function called")
    hunger_status(hunger,lang)
    hp_status(hp,lang)

# Describes the surrounding environment and the items in it
def surroundings(loc,environ,ground,lang): # TODO: test
    log("output.py surroundings()","function called")
    print("surroundings()")
    loc(loc,lang)
    environ(environ,lang)
    ground(ground,lang)
    time.sleep(constant.DELAY)

def welcome(lang):
    log("output.py welcome()","function called")
    custom(constant.WELCOME_EXPR,'!',lang)
    time.sleep(constant.DELAY)