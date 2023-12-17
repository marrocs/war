import functions, settings, re



def main():


    print('-----> Welcome to War Games <-----')
    

    # Get players
    functions.receive_guests()
    
    # Initiate the Party and append it to current_party list
    
    functions.create_party(settings.players_list)


    while settings.current_party[0].status is True:

        print("Around the world, around-the-wooooorld") # Weird thing happening here: infinity loop. Further code is ignored    
        
        # Get action for every player
        for turn_player in settings.players_list:
            
            print("olha eu aqui")

            
            if turn_player.name[0:8] == "machine_":
                functions.machine_movement(turn_player)

            else:
                functions.get_action(turn_player, functions.menu_action(turn_player))
            
        # Read and execute action queue
        functions.queue_cleaner(settings.action_queue)

        # After clean action_queue, add 1 to party round
        settings.current_party[0].round += 1
    
    else:
        print("ENDGAME")
        exit()

if __name__ == '__main__':
    main()