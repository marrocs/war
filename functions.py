from models import *
import db
import main

def create_party(players_list):

    players = [p for p in players_list]

    for p in players:
        reyalp = Player(p)

        db.players.append(reyalp)

    main.current_party.append(Party(db.players))

    print(f'Party nº {main.current_party[0].id} initiated with: {db.players}')

    return main.current_party[0]
        

def menu_action(player) -> None:
    print(f"\n\nHello {player.name}, here's what you need to know:\n ")
    print(f'This is round {main.current_party[0].round}\n\n')
    player.show_infos()

    print("\n\nYou might: \n\n1-Invest\n2-Buy military\n3-Attack\n4-Pass\n\n")

    return None


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

        print("ENDGAME")
        exit()

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
#     next()


def queue_cleaner(queue):
    for action in queue:

        if action.exec_round == main.current_party[0].round:
            action_in_execution = globals().get(action.type)

            action_in_execution(action)
        else:
            continue

    main.current_party[0].round += 1


def get_time():


    pass


def generate_log():
    pass