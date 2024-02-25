import utils.functions as functions, settings



def main():


    print('-----> Welcome to War Games <-----')
    

    # Get players
    functions.receive_guests()
    
    # Initiate the Party and append it to current_party list
    
    functions.create_party(settings.players_list)


    #while len(settings.players_list) >= 1:
    while settings.current_party[0].status is True:

        # Get action for every player
        for turn_player in settings.players_list:
            
            if turn_player.name[0:8] == "machine_":
                functions.machine_movement(turn_player)

            else:
                functions.get_action(turn_player, functions.menu_action(turn_player))
            
        # Read and execute action queue
        functions.queue_cleaner(settings.action_queue)

        # After clean action_queue, add 1 to party round
        settings.current_party[0].round += 1
    
    
    #settings.current_party[0].status = False
    functions.end_party(settings.current_party[0])
    print("ENDGAME")
    exit()

if __name__ == '__main__':
    main()