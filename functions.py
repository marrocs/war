from models import *
import db
import settings

def receive_guests() -> str:

    try:
        guests_names = []

        #guests_names.append(input("\n\nWelcome. Enter your name: "))

        #more_player = input(f"There is {len(guests_names)} players. You can add up to 4 players. Want to add another player? y/n \n\n")

        num_players = int(input("How many players? "))

        # 04/11 -  Aqui esta dando problema
        for x in range(num_players):

            name = input(f"Player's {x+1} name: ")
            guests_names.append(name)
            print(f"\nThere will be {num_players} players \n")
            print(f"Player {name} registered for party")
            
        # Instanciate Players with names and Append Players to settings.players_list

        for p in guests_names:
            new_player = Player(p)

            # Isso aqui não esta funcionando. Players list não está sendo populado
            settings.players_list.append(new_player)
            
    
    except:
        #break()
        return "400 ERROR"

    
    return "200 OK"
   
def create_party(players_list) -> list:

    try:
        
        new_party = Party(players_list)
        
        settings.current_party.append(new_party)  # --> Isso daqui não está funcionando

        print(f'Party nº {settings.current_party[0].id} initiated with: {settings.current_party[0].players}')

    except:
        return "400 ERROR"
    
    return "200 OK"
        

def menu_action(player) -> str:
    print(f"\n\nHello {player.name}, here's what you need to know:\n ")
    print(f'This is round {settings.current_party[0].round}\n\n')
    player.show_infos()

    print("\n\nYou might: \n\n1-Invest\n2-Buy military\n3-Attack\n4-Pass\n\n")

    action = input('Your choice: ')

    return f"200 {action}"


def get_action(player, return_code) -> str:

    splited_return_code = return_code.split(' ')
    action = int(splited_return_code[1])

    # Invest
    if action == 1:

        quantity_to_invest = input("How much to invest?")

        while int(quantity_to_invest) > int(player.money):

            print("You don't have all that. Try again.")
            #quantity_to_invest = input("How much to invest?")

            return "400 ERROR"

        else:

            investment_time = input("How many turns money should be invested?")

            invest_action = Action(settings.current_party[0].round, executor=player, target=player, type="invest", quantity=quantity_to_invest, ttl=investment_time)
            settings.action_queue.append(invest_action)

            print(f'You have invested ${quantity_to_invest}!')

            return "200 OK"
        
    # Hire
    elif action == 2:

        quantity_to_hire = input("how many soldiers to hire?")
        price = int(quantity_to_hire) * 2

        while price > int(player.money):

            print("You don't have all that. Try again.")

            return "400 ERROR"

        else:

            hire_action = Action(settings.current_party[0].round, executor=player, target=player, type="hire", quantity=quantity_to_hire, ttl=1)
            settings.action_queue.append(hire_action)
            print(f'You have asked for ${quantity_to_hire} soldiers!')

            return "200 OK"

    # Attack
    elif action == 3:

        print("These are the other players: \n\n")
                
        for x in settings.players_list:

            if x.name == player.name:
                return "400 ERROR"
            
            else:
                print(x.name)

        target_player = input("Who do you attack?")

        while target_player == player:

            print("You can't attack yourself")
            
            return "400 ERROR"

        else:

            force_employed = input("\n\nHow many soldiers will be deployed?")

            while int(player.military) < int(force_employed):

                print("You don't have all that. Try again.")
                
                return "400 ERROR"

            else:

                attack_action = Action(settings.current_party[0].round, executor=player, target=target_player, type="attack", quantity=force_employed, ttl=2)
                settings.action_queue.append(attack_action)
                print(f'You sent {force_employed} soldiers to attack {attack_action.target}!')

                return "200,OK"
            
    # Pass
    elif action == str(4):
        return "200 OK"
                    

def invest(action):

    invested_value = action.quantity
    interest_rate = 1
    time_investment = action.ttl
    investment_return = int(invested_value) * int(time_investment) * int(interest_rate)

    action.executor.money += investment_return
                
    print(f'{action.executor} just received ${investment_return} back!')
    
    return None


def hire(action):

    quantity_to_hire = int(action.quantity)
    benefited = action.executor
    actual_num_troops = int(benefited.military)

    benefited.military = str(quantity_to_hire + actual_num_troops)
    print(f"Good news. The {quantity_to_hire} soldiers you requested has arrived.")

    return None


def attack(action):
    
    offensive_player = action.executor
    defensive_player = action.target
    offensive_force = offensive_player.military
    defensive_army = defensive_player.military

    if int(defensive_army) == 0:

        print(f"ENDGAME for {defensive_player}")
        settings.current_party.status = False

    else:

        if int(offensive_force) > int(defensive_army):
            
            soldiers_survives = int(offensive_force) - int(defensive_army)

            defensive_player.military = 0
            offensive_player.military = int(offensive_player.military) + int(soldiers_survives)

            print(f"You win and {soldiers_survives} soldiers has returned from battlefield")

        else:
            
            soldiers_survives = 0
            defense_result = int(defensive_player.military) - int(offensive_force)
            offensive_player.military = int(offensive_player.military) - (offensive_force)

            defensive_player.military = defense_result

            print(f"You lost all the soldiers you sent")


# def call_next_round():
#     continue


def queue_cleaner(queue):
    for action in queue:

        if action.exec_round == settings.current_party[0].round:
            action_in_execution = globals().get(action.type)

            action_in_execution(action)

            return "200 OK"
        
        else:
            
            return "400 ERROR"

    settings.current_party[0].round += 1


def get_time():


    pass


def generate_log():
    pass