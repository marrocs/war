import utils.functions as functions, settings
from time import sleep


def main():


    print('-----> Welcome to War Games <-----')
    

    # Get players
    functions.receive_guests()
    
    # Initiate the Party and append it to current_party list
    
    functions.create_party(settings.players_list)


    #while len(settings.players_list) >= 1:
    while settings.current_party[0].status is True:
        
        '''
        Aqui devem estar as tarefas a serem executadas todas as rodadas;
        '''

        print(f"\n\n -----> This is Round {settings.current_party[0].round} <-----\n")
        
        # TASK: Get orders
        for turn_player in settings.players_list:
            
            if turn_player.name[0:8] == "machine_":
                functions.machine_movement(turn_player)

            else:
                functions.get_action(turn_player, functions.menu_action(turn_player))
                
            print(turn_player.main_status())
            
        # TASK: Read and execute orders in line
        functions.parser(settings.action_queue)
        
        # TASK: bill players for civillian and military maintance
        functions.bill_atributes(settings.players_list)
        
        # TASK: Check if there are other players on party
        if len(settings.players_list) == 1:
            
            settings.current_party[0].winner = settings.players_list[0].name

            functions.shut_party(settings.current_party[0])            
            
            return "200 OK"

        # TASK: Update round countage
        settings.current_party[0].round += 1
        
        # No-need task: wait 1s
        sleep(settings.SLEEP_TIME_BETWEEN_ROUNDS)
    
    
    #settings.current_party[0].status = False
    functions.shut_party(settings.current_party[0])
    print("ENDGAME")
    exit()

if __name__ == '__main__':
    main()