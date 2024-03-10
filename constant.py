# Do not add function names to this file that are not in Adventure.gf and linearized in all language grammar files Adventure[Lang].gf

# Output delay
DELAY = 0.05

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
STARVING_HP_LOSS_RATE = 2

# environments
ENVIRON_TYPES = ['snowfield_Loc','ocean_Loc'] #TODO: Add 'mountain_Loc'
SNOW_FIELD_ITEMS = ['snow_Feat','rock_Feat','ice_Feat']
OCEAN_ITEMS = ['fish_Feat'] # Change to weighted generation in helper.gen_ground_items() if more items added to this list

# action types
COMMAND_FUNCS = ['VComm','VDetComm','V2DetComm']
NAVIGATION_FUNCS = ['VDirComm','V2DirComm']
HAVE_FUNCS = [] # inquiries about inventory contents or hunger/HP stats

# other expressions
ARENT_ANY_EXPR = 'ArentAny'
CURRENT_LOC_EXPR = 'ArePrepLoc you_Pron at_Prep missingdet_Det location_Loc'
DEATH_EXPR = 'Death'
DONT_HAVE_EXPR = 'PronDontV2AnyFeat you_Pron have_V2' # +Feat
ENVIRON_EXPR = 'ArePrepLoc you_Pron at_Prep' # +Det +Loc
#FEAT_EXPR = 'FeatAlone' # +Feat
GOODBYE_EXPR = 'Goodbye'
HP_EXPR = 'FeatAlone hp_Feat'
HUNGER_EXPR = 'FeatAlone hunger_Feat'
INVALID_INPUT_EXPR = 'Invalid'
INV_EXPR = 'FeatAlone inventory_Feat'
INV_EMPTY_EXPR = 'YourFeatIsA inventory_Feat empty_A'
INV_FULL_EXPR = 'YourFeatIsA inventory_Feat full_A'
MOVE_LOC_EXPR = 'PronV2PrepLoc you_Pron move_V2 to_Prep location_Loc' # loc tuple
PICK_UP_EXPR = 'PronV2DetFeat you_Pron pickup_V2' # +Det +Feat
SEE_EXPR = 'PronV2DetFeat you_Pron see_V2' # +Det +Feat
SEE_NOTHING_EXPR = 'SeeNothing'
WELCOME_EXPR = 'Welcome'

# cardinal directions
NORTH = ['n_Dir','north_Dir']
SOUTH = ['s_Dir','south_Dir']
EAST = ['e_Dir','east_Dir']
WEST = ['w_Dir','west_Dir']

# objects
FOOD_WORDS = ['fish_Feat']

# verbs
DROP_WORDS = ['drop_V2','putdown_V2','setdown_V2']
EAT_WORDS = ['consume_V','consume_V2','eat_V','eat_V2']
HELP_WORDS = ['help_V','help_V2']
PICK_UP_WORDS = ['carry_V2','catch_V2','gain_V2','gather_V2','get_V2','grab_V2','lift_V2','pickup_V2','take_V2']
QUIT_WORDS = ['quit_V','quit_V2','exit_V','exit_V2']

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
# ALL = ['all_Det','these_Det','those_Det','every_Det'] # TODO: Implement in helper.py
# UNKNOWN = ['afew_Det','some_Det','more_Det'] # TODO: Implement in helper.py
NUMS = [ZERO,ONE,TWO,THREE,FOUR,FIVE,SIX,SEVEN,EIGHT,NINE,TEN]

# proper nouns (if some added, TODO: use for capitalization in postprocessing)
PLACES = []
NAMES = []

# acronyms (TODO: in all caps in postprocessing)
ALL_CAPS = ['hp_Stat']