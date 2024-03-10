import helper
import constant
import output

# Removes some amount of specified item from inventory and drops them to the ground
def drop(ground,inv,det_amt,item,lang):
    output.log("event.py drop()","function called")
    inv_amt = helper.count_inv_item(inv,item)
    if det_amt > inv_amt : # requested to drop more items than have in inv.
        amt = inv_amt
    else:
        amt = det_amt
    if amt > 0 : # there is some amount of items that can be dropped
        helper.remove_from_inv(inv,item,amt)
        helper.add_to_ground(ground,item,amt)
    return ground,inv

# Removes indicated food from inventory and increases hunger and hp
def eat(ground,inv,hunger,hp,det_amt,food,lang):
    output.log("event.py eat()","function called")
    for food in constant.FOOD_WORDS:
        if helper.is_in_inv(inv,food):
            output.log("event.py eat()","test point 2 reached")
            inv = helper.remove_from_inv(inv,food,det_amt)
            hunger = helper.gain_hunger(hunger,constant.FOOD_HUNGER_GAIN_RATE * det_amt) # gain hunger
            hp = helper.gain_hp(hp,constant.FOOD_HP_GAIN_RATE * det_amt) # gain hp
            return inv,hunger,hp
        # elif is_on_ground(ground,food): (USE INSTEAD -> count_ground_item(ground,target))
            #TODO: Check if any of the food is on the ground
            #If so, eat food like before (TODO: MAKE SEPARATE FUNCTION eat())
            #return inv,hunger,hp
    output.dont_have(food,lang)
    return inv,hunger,hp

def help(lang): # TODO: implement function
    output.log("event.py help()","function called")

def pick_up(ground,inv,det_amt,obj,lang): # TODO: Finish testing
    output.log("event.py pick_up()","function called")
    ground_amt = helper.count_ground_item(ground,obj)
    if ground_amt == 0: # nothing on ground to pick up
        return ground,inv
    elif det_amt > ground_amt:
        amount = ground_amt # add/remove ground_amt of item to inv/from ground
    else:
        amount = det_amt # add/remove det_amt of item to inv/from ground
    inv = helper.add_to_inv(inv,obj,amount)
    ground = helper.remove_from_ground(ground,obj,amount)
    output.pick_up(det_amt,obj,lang)
    return ground,inv

def quit(lang):
    output.log("event.py quit()","function called")
    output.goodbye(lang)