global players_list, action_queue, current_party


# <-----> OBJECT HOLDERS <----->
players_list = [] # Must receive Player.
action_queue = [] # Must receive Action 
current_party = [] # Must receive only one object Party 


# <-----> GAME SETTINGS <----->
CIVILIAN_INJURY_RATE=2.1
CIVILIAN_PRODUCTIVITY=0.75
MILITARY_PRICE=3.0
CIVILLIAN_PRICE=1.5
MILITARY_MAINTANCE=1.5
CIVILLIAN_MAINTANCE=0
INTEREST_RATE=0.8
TERRAIN_ADVANTAGE=0
SLEEP_TIME_BETWEEN_ROUNDS=0.3



# <-----> MACHINE SETTINGS <----->
MACHINE_DIFICULT=0
MACHINE_MIN_CIVILLIANS=100
MACHINE_MIN_MONEY=400
MACHINE_MIN_MILITARY=100
