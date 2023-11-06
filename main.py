import functions 

global players_list 
global action_queue
global current_party

# <-----> OBJECT HOLDERS <----->
players_list = [] # Must receive Player. Also, must be here, not in functions.
action_queue = [] # Must receive Action 
current_party = [] # Must receive only one object Party 
# <-----> END OBJECT HOLDERS <----->

def main():


    print('-----> Welcome to War Games <-----')
    

    # Get players
    functions.receive_guests()
    
    # Initiate the Party and append it to current_party list
    functions.create_party(players_list)


    while current_party[0].status is True:

        
        # Get action for every player
        for turn_player in players_list:

            functions.get_action(turn_player, functions.menu_action(turn_player))
            
        # Read and execute action queue
        functions.queue_cleaner(action_queue)
    
    else:
        print("ENDGAME")
        exit()

if __name__ == '__main__':
    main()