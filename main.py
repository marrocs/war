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

    current_party.append(this_party)


    while current_party[0].status is True:

        
        # Get action for every player
        for turn_player in db.players:

            menu_action(turn_player)

            action = input('Your choice: ')

            # Invest
            if action == str(1):
                quantity_to_invest = input("How much to invest?")
                investment_time = input("How many turns money should be invested?")

                while int(quantity_to_invest) > int(turn_player.money):

                    print("You don't have all that. Try again.")
                    quantity_to_invest = input("How much to invest?")

                else:

                    invest_action = Action(current_party[0].round, executor=turn_player, target=turn_player, type="invest", quantity=quantity_to_invest, ttl=investment_time)
                    action_queue.append(invest_action)
                    print(f'You have invested ${quantity_to_invest}!')
            
            # Hire
            elif action == str(2):

                quantity_to_hire = input("how many soldiers to hire?")
                price = int(quantity_to_hire) * 2

                while price > int(turn_player.money):

                    print("You don't have all that. Try again.")

                    quantity_to_hire = input("how many soldiers to hire?")

                else:

                    hire_action = Action(current_party[0].round, executor=turn_player, target=turn_player, type="hire", quantity=quantity_to_hire, ttl=1)
                    action_queue.append(hire_action)
                    print(f'You have asked for ${quantity_to_hire} soldiers!')
            
            # Attack
            elif action == str(3):

                print("These are the other players: \n\n")
                
                for x in players_list:

                    if x == turn_player:
                        continue
                    else:
                        print(x)

                target_player = input("Who do you attack?")

                while target_player == turn_player:

                    print("You can't attack yourself")
                    target_player = input("\n\nWho do you attack?\n")

                else:

                    force_employed = input("\n\nHow many soldiers will be deployed?")

                    while int(turn_player.military) < int(force_employed):

                        print("You don't have all that. Try again.")
                        force_employed = input("\n\nhow many soldiers to send?")

                    else:

                        attack_action = Action(current_party[0].round, executor=turn_player, target=target_player, type="attack", quantity=force_employed, ttl=2)
                        action_queue.append(attack_action)
                        print(f'You sent ${force_employed} soldiers to attack {attack_action.target}!')
            
            # Pass
            elif action == str(4):
                continue
        
        # Read and execute action queue
        queue_cleaner(action_queue)
        

if __name__ == '__main__':
    main()