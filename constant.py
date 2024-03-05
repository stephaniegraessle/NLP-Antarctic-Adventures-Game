# Inventory/needs maximum sizes
INVENTORY_SIZE = 10
MAX_HP = 10
MAX_HUNGER = 10

# Hunger gain/loss rates
ACTION_HUNGER_LOSS_RATE = 2
FOOD_HUNGER_GAIN_RATE = 5
NORMAL_HUNGER_LOSS_RATE = 1

# HP gain/loss rates
FOOD_HP_GAIN_RATE = 5
STARVING_HP_LOSS_RATE = 1

# environments
ENVIRON_TYPES = ['snow field','ocean'] #TODO: Add 'mountain
SNOW_FIELD_ITEMS = ['snow_Feat','rock_Feat','ice_Feat']
OCEAN_ITEMS = ['fish_Feat'] # Change to weighted generation in helper.gen_ground_items() if more items added to this list

# action types
COMMAND_FUNCS = ['V2DetComm','VComm']
NAVIGATION_FUNCS = ['VDirComm','V2DirComm']

# objects
FOOD_WORDS = ['fish_Feat']

# cardinal directions
NORTH = ['n_Dir','north_Dir']
SOUTH = ['s_Dir','south_Dir']
EAST = ['e_Dir','east_Dir']
WEST = ['w_Dir','west_Dir']

# verbs
EAT_WORDS = ['consume_V','consume_V2','eat_V','eat_V2']
PICK_UP_WORDS = ['carry_V2','gain_V2','get_V2','grab_V2','lift_V2','pickup_V2']
DROP_WORDS = ['drop_V2','putdown_V2','setdown_V2']

# determiners
ZERO = ['no_Det','zero_Det','zero_num_Det']
ONE = ['one_Det','one_num_Det','a_Det','an_Det','a_n_Det','missingdet_Det','that_Det','the_Det','this_Det']
TWO = ['acouple_Det','two_Det','two_num_Det']
THREE = ['three_Det','three_num_Det']
FOUR = ['four_Det','four_num_Det']
FIVE = ['five_Det','five_num_Det']
SIX = ['six_Det','six_num_Det']
SEVEN = ['seven_Det','seven_num_Det']
EIGHT = ['eight_Det','eight_num_Det']
NINE = ['nine_Det','nine_num_Det']
TEN = ['ten_Det','ten_num_Det']
NUMS = [ZERO,ONE,TWO,THREE,FOUR,FIVE,SIX,SEVEN,EIGHT,NINE,TEN]

# proper nouns (if some added, TODO: use for capitalization in postprocessing)
PLACES = []
NAMES = []