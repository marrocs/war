from functions import *
import db

global players_list 
global action_queue
global current_party


players_list = [] # Must receive Player. Also, must be here, not in functions.
action_queue = [] # Must receive Action
current_party = [] # Must receive only one object Party

def main():


    print('-----> Welcome to War Games <-----')
    

    # Get players
    receive_guests()
    
    # Initiate the Party and append it to current_party list
    current_party.append(create_party(players_list))


    while current_party[0].status is True:

        
        # Get action for every player
        for turn_player in players_list:

            get_action(turn_player, menu_action(turn_player))
            
        # Read and execute action queue
        queue_cleaner(action_queue)
    
    else:
        print("ENDGAME")
        exit()

if __name__ == '__main__':
    main()