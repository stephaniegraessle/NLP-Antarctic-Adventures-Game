import random

# Input: current location as list [x,y] and direction moving in
# Output: new location
def move(loc, dir) :
    # when east, x+1
    # when north, y+1
    # when west, x-1
    # when south, y-1
    return loc

# Output: A random environment
def gen_environ():
    environ_types = ["snow field","ocean"]
    environ = random.choices(environ_types, weights=(80,20),k=1)[0] # gen environ, more likely to travel to "snow field" than "ocean"
    # TODO: Generate a random function indicating shoreline. Points on one side of line are snow field, those on the other are the ocean.
    return environ