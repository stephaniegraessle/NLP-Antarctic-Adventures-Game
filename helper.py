import random
import time
import constant
import output

# Determines new coordinate location as list [x,y] after moving, generates new environment for previously unexplored areas
# Input: map dictionary, current location as list [x,y], and direction moving in
# Output: new location
def move(loc,dir) :
    try:
        x = loc[0]
        y = loc[1]

        if dir in constant.EAST: # x-value + 1
            x = x + 1
        elif dir in constant.NORTH: # y-value + 1
            y = y + 1
        elif dir in constant.WEST: # x-value - 1
            x = x - 1
        elif dir in constant.SOUTH: # y-value - 1
            y = y - 1
        else: # no change
            return loc

        loc=(x,y) # update to new loc
        
        # TODO: Create map to remember where been before. Cannot use list as map key.
        # if location already in map (already been to location)
        #if loc in map.keys():
        #    return loc
        #else: #if not already in map, gen. new environment
        #    info = gen_environ(loc,lang)
        #    map.update({loc:info}) # add to map
    except:
        output.log("helper.py move()","failed")
    return loc # return modified location

# Output: A random environment from environment types list
# TODO: Generate a random function indicating shoreline. Points on one side of line are snow field, those on the other are the ocean.
def determine_environ():
    try:
        environ = random.choices(constant.ENVIRON_TYPES, weights=(60,40),k=1)[0] # gen environ, more likely to travel to "snow field" than "ocean"
        return environ
    except:
        output.log("helper.py determine_environ()","failed")

# Generates a list of interactable items in a given environment
# Input: environ string
# Output: list of items in the environment
def gen_ground_items(environ): # TODO: Test if item names are linearized correctly
    try:
        ground = []
        amount = random.randrange(2,7) # determine how many items to generate
        if environ == 'ocean_Loc':
            # ground = random.choices(constant.OCEAN_ITEMS, weights=(100),k=amount)
            for i in range(amount):
                item = random.choice(constant.OCEAN_ITEMS)
                ground.append(item)
        elif environ == 'snowfield_Loc':
            ground = random.choices(constant.SNOW_FIELD_ITEMS, weights=(65,15,10),k=amount)
        return ground # empty if unknown environment or no items generated
    except:
        output.log("helper.py gen_ground_items()","failed")

# Checks if a given target item is on the ground
# Input: list of items on ground, target item
# Output: Number of items on the ground
def count_ground_item(ground,item):
    try:
        return ground.count(item)
    except:
        output.log("helper.py count_ground_items()","failed")

def remove_from_ground(ground,item,amount):
    try:
        ground_amt = count_ground_item(ground,item)
        if amount > ground_amt:
            amount = ground_amt
        for a in range(0,amount):
            ground.remove(item)
        # TODO: Statement of how many items were removed from ground.
        return ground
    except:
        output.log("helper.py remove_from_ground()","failed")

# Adds an indicated item of a certain amount to the ground
# Output: ground list
def add_to_ground(ground,item,amount):
    try:
        while amount > 0:
            ground.append(item)
            amount -= 1
        # TODO: Statement of how many items were added to ground.
    except:
        output.log("helper.py add_to_ground()","failed")
    return ground

def gen_environ(loc,lang): # TODO: Test
    environ = determine_environ() # init starting environment
    ground = gen_ground_items(environ) # generate items on ground based on environment type
    output.environ(environ,lang)
    return [environ, ground]

# Increase the hunger value by a given amount
# Input: hunger, amount to increase hunger by
# Output: new hunger value
def gain_hunger(hunger,amount): # TODO: Test
    try:
        newhunger = hunger + amount
        if newhunger >= constant.MAX_HUNGER:
            return constant.MAX_HUNGER
        else:
            return newhunger
    except:
        output.log("helper.py gain_hunger()","failed")
        return hunger

# Decrease the hunger value by a given amount
# Input: hunger, amount by which to decrease the hunger
# Output: new hunger value
def lose_hunger(hunger,amount):
    try:
        if hunger >= amount:
            hunger-=amount # lose amount of hunger specified in argument
        elif hunger < amount:
            hunger = 0 # cannot have negative hunger
    except:
        output.log("event.py drop()","failed")
    return hunger

# Check whether penguin is starving (hunger == 0)
# Input: hunger, hp
# Output: static or lowered hp
def check_if_starving(hunger,hp):
    try:
        if hunger == 0: # starving
            hp = lose_hp(hp,constant.STARVING_HP_LOSS_RATE)
        return hp
    except:
        output.log("helper.py check_if_starving()","failed")

# Lower HP by given amount
# Input: hp, amount to decrease by
# Output: new hp value
def lose_hp(hp,amount):
    try:
        if hp-amount < 0:
            hp = 0
        else:
            hp = hp-amount
        return hp
    except:
        output.log("helper.py lose_hp()","failed")
    
# Gain HP by given amount
# Input: hp, amount to increase by
# Output: new hp value
def gain_hp(hp,amount): # TODO: Test
    try:
        if hp + amount > constant.MAX_HP:
            return constant.MAX_HP
        else:
            return hp + amount
    except:
        output.log("helper.py gain_hp()","failed")

def check_if_dead(hp,lang):
    try:
        if hp <= 0: # dead
            output.death(lang)
            return True
        return False # alive
    except:
        output.log("helper.py check_if_dead()","failed")

# Checks if the inventory has enough room to add more items
# Input: inventory dictionary
# Output: True if has more room, False if inventory is full
def has_inv_space(inv): # TODO: Test--need to have full inventory
    try:
        size = len(inv)
        if size < constant.INVENTORY_SIZE:
            return True # inventory has more room
        # add statement
        return False # inventory is full
    except:
        output.log("helper.py has_inv_space()","failed")

# Checks if a given item is already in the inventory
# Input: Inventory dictionary, string item
# Output: True if item already in inventory, False if not
def is_in_inv(inv,item): # TODO: Test
    try:
        #if item in inv:
        if item in inv.keys():
            return True
        # TODO: Add statement
        return False
    except:
        output.log("helper.py is_in_inv()","failed")

# Checks how many of a given item are in the inventory
# Input: inventory list, string target item
# Output: Integer number of how many of the target item is in the inventory
def count_inv_item(inv,item):
    try:
        if item in inv.keys():
            return inv[item]
        return 0
    except:
        output.log("helper.py count_inv_item()","failed")

# Adds a new item of a given amount to the inventory
# Input: inventory dictionary, item string, amount integer
# Output: if inventory has space, returns updated inventory with new item
def add_to_inv(inv,item,amount):
    try:
        inv_amount = count_inv_item(inv,item)
        if inv_amount == 0 and has_inv_space(inv): # none of item already in inv and inv has more space
            inv.update({item:amount}) # add new item to inventory
        elif inv_amount > 0: # some of item already in inventory
            inv.update({item:inv_amount+amount}) # add items onto existing amount in inv
        # TODO: Add statement saying what was added to inventory
        return inv # no changes made to inv
    except:
        output.log("helper.py add_to_inv()","failed")

# Removes some item from inventory by a given amount
# Input: inventory dictionary, item string, amount integer
# Output: updated inventory with removed item
def remove_from_inv(inv,item,amount):
    try:
        if is_in_inv(inv,item): # if item already not in inventory, no changes made 
            inv_amount = count_inv_item(inv,item)
            if inv_amount <= amount:
                inv.pop(item)
            else:
                inv.update({item:inv_amount-amount})
        # TODO: Add statement saying what was removed from inventory
    except:
        output.log("helper.py remove_from_inv()","failed")
    return inv
