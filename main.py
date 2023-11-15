import functions, settings



def main():


    print('-----> Welcome to War Games <-----')
    

    # Get players
    functions.receive_guests()
    
    # Initiate the Party and append it to current_party list
    
    functions.create_party(settings.players_list)


    while settings.current_party[0].status is True:

        
        # Get action for every player
        for turn_player in settings.players_list:

            functions.get_action(turn_player, functions.menu_action(turn_player))
            
        # Read and execute action queue
        functions.queue_cleaner(settings.action_queue)
    
    else:
        print("ENDGAME")
        exit()

if __name__ == '__main__':
    main()