import random
import constant

# Prints current hunger and HP values
# Input: hunger and hp integers
def print_stats(hunger,hp):
    print("Hunger:",hunger)
    print("HP:",hp)

# Prints current inventory  contents
# Input: inventory dictionary
def print_inv(inv):
    print(inv.values())

# Input: current location as list [x,y] and direction moving in
# Output: new location
def move(loc, dir) : # TODO: Complete & test
    # when east, x+1
    # when north, y+1
    # when west, x-1
    # when south, y-1
    return loc

# Output: A random environment from environment types list
# TODO: Generate a random function indicating shoreline. Points on one side of line are snow field, those on the other are the ocean.
def gen_environ(): # TODO: Testing
    environ_types = ["snow field","ocean"]
    environ = random.choices(environ_types, weights=(80,20),k=1)[0] # gen environ, more likely to travel to "snow field" than "ocean"
    return environ

# Increase the hunger value by a given amount
# Input: hunger, amount to increase hunger by
# Output: new hunger value
def gain_hunger(hunger,amount): # TODO: Test
    if hunger + amount > 100:
        hunger == 100 # cannot have hunger > 100
    else:
        hunger = hunger + amount
    return hunger

# Decrease the hunger value by a given amount
# Input: hunger, amount by which to decrease the hunger
# Output: new hunger value
def lose_hunger(hunger,amount):
    if hunger >= amount:
        hunger-=amount # lose amount of hunger specified in argument
    elif hunger < amount:
        hunger = 0 # cannot have negative hunger
    return hunger

# Check whether penguin is starving (hunger == 0)
# Input: hunger, hp
# Output: static or lowered hp
def check_if_starving(hunger,hp):
    if hunger == 0: # starving
        hp = lose_hp(hp,constant.STARVING_HP_LOSS_RATE)
    return hp

# Lower HP by given amount
# Input: hp, amount to decrease by
# Output: new hp value
def lose_hp(hp,amount):
    if hp-amount < 0:
        hp = 0
    else:
        hp = hp-amount
    return hp
    
# Gain HP by given amount
# Input: hp, amount to increase by
# Output: new hp value
def gain_hp(hp,amount): # TODO: Test
    if hp+amount > constant.MAX_HP:
        return constant.MAX_HP
    else:
        return hp + amount

# Checks how many of a given item are in the inventory
# Input: inventory list, string target item
# Output: Integer number of how many of the target item is in the inventory
def check_inv_item(inv, target): # TODO: Testing
    for item in inv:
        if item == target:
            return 1
    return 0

# Checks if the inventory has enough room to add more items
# Input: inventory dictionary
# Output: True if has more room, False if inventory is full
def has_inv_space(inv): # TODO: Test
    size = len(inv)
    if size < constant.INVENTORY_SIZE:
        return True # inventory has more room
    return False # inventory is full

# Checks if a given item is already in the inventory
# Input: Inventory dictionary, string item
# Output: True if item already in inventory, False if not
def is_in_inv(inv,item): # TODO: Test
    #if item in inv:
    if item in inv.keys():
        return True
    return False

# Adds a new item of a given amount to the inventory
# Input: inventory dictionary, item string, amount integer
# Output: if inventory has space, returns updated inventory with new item
def add_to_inv(inv,item,amount): # TODO: Test
    if is_in_inv(item): # check if item already in inventory
        # add to current item already in inventory
        inv_amount = inv[item]
        inv.update({item:inv_amount+amount}) # update existing item
    elif has_inv_space(inv):
        inv.update({item:amount}) # add new item to inventory

# Removes some item from inventory by a given amount
# Input: inventory dictionary, item string, amount integer
# Output: updated inventory with removed item
def remove_from_inv(inv,item,amount): # TODO: Test
    if is_in_inv(item): # item found in inventory
        inv_amount = inv[item] # get amount of the item already in the inventory
        if inv_amount <= amount:
            inv.update({item:0}) # cannot have negative amount, lowest is 0
        else:
            inv.update({item:inv_amount-amount})
    # if item already not in inventory, no changes made
    return inv

        

