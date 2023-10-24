from functions import *
import db

global players_list 
global action_queue
global current_party


players_list = []
action_queue = []
current_party = []

def main():


    print('-----> Welcome to War Games <-----')



    # Get players

    player_1 = input("Player 1 name: ")
    player_2 = input("Player 2 name: ")
    
    players_list.append(player_1)
    players_list.append(player_2)
    
    # Initiate the party
    this_party = create_party(players_list)

    while this_party.status is True:
        
        # Get action for every player
        for turn_player in db.players:

            menu_action(turn_player)

            action = input('Your choice: ')

            # Invest
            if action == 1:
                quantity_to_invest = input("How much to invest?")
                investment_time = input("How many turns money should be invested?")

                while quantity_to_invest > turn_player.money:

                    print("You don't have all that. Try again.")
                    quantity_to_invest = input("How much to invest?")

                else:

                    invest_action = Action(main.current_party.round, executor=turn_player, target=turn_player, type="invest", quantity=quantity_to_invest, ttl=investment_time)
                    main.action_queue.append(invest_action)
                    print(f'You have invested ${quantity_to_invest}!')
            
            # Hire
            elif action == 2:

                quantity_to_hire = input("how many soldiers to hire?")
                price = quantity_to_hire * 2

                while price > turn_player.money:

                    print("You don't have all that. Try again.")
                    quantity_to_hire = input("how many soldiers to hire?")

                else:

                    hire_action = Action(main.current_party.round, executor=turn_player, target=turn_player, type="hire", quantity=quantity_to_hire, ttl=1)
                    main.action_queue.append(hire_action)
                    print(f'You have asked for ${quantity_to_hire} soldiers!')
            
            # Attack
            elif action == 3:
                
                print(x.name for x in players_list)

                target = input("Who do you attack?")

                while target == action.executor:

                    print("You can't attack yourself")
                    target_player = input("Who do you attack?")

                else:

                    force_employed = input("How many soldiers will be sent?")

                    while action.executor.military < force_employed:

                        print("You don't have all that. Try again.")
                        force_employed = input("how many soldiers to send?")

                    else:

                        attack_action = Action(main.current_party.round, executor=turn_player, target=target_player, type="hire", quantity=force_employed, ttl=2)
                        main.action_queue.append(attack_action)
                        print(f'You sent ${force_employed} soldiers to attack {attack_action.target}!')
            
            # Pass
            elif action == 4:
                call_next_round()
        
        # Read and execute action queue
        queue_cleaner(action_queue)
        current_party[0].round += 1

if __name__ == '__main__':
    main()