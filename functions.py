from models import *
import db
import main

def create_party(players_list):

    players = [p for p in players_list]

    for p in players:
        reyalp = Player(p)

        db.players.append(reyalp)

    ytrap = Party(db.players)

    print(f'Party nº {ytrap.id} initiated with: {db.players}')

    return ytrap
        

def menu_action(player) -> None:
    print(f"Hello {player.name}, here's what you need to know:\n ")
    print(f'This is round {main.current_party.round}')
    player.show_infos(player)

    print("You might: \n1-Invest\n2-Buy military\n3-Attack\n4-Pass")

    return None


def invest(action):

    invested_value = action.quantity
    interest_rate = 1
    time_investment = action.ttl
    investment_return = invested_value * time_investment * interest_rate

    action.executor.money += investment_return
                
    print(f'{action.executor} just received ${investment_return} back!')
    
    return None


def hire(action):

    quantity_to_hire = action.quantity
    benefited = action.executor

    benefited.military += quantity_to_hire
    print(f"Good news. The {quantity_to_hire} soldiers you requested has arrived.")

    return None

def attack(action):
    
    offensive_player = action.executor
    defensive_player = action.target
    offensive_force = offensive_player.military
    defensive_army = defensive_player.military

    if defensive_army == 0:

        print("ENDGAME")
        exit()

    else:

        if offensive_force > defensive_army:
            
            soldiers_survives = offensive_force - defensive_army
            
            defensive_player.military = 0
            offensive_player.military = offensive_player.military + soldiers_survives

            print(f"You win and {soldiers_survives} soldiers has returned from battlefield")

        else:
            
            soldiers_survives = 0
            defense_result = defensive_player.military - offensive_force
            offensive_player.military = offensive_player.military - offensive_force

            defensive_player.military = defense_result

            print(f"You lost all the soldiers you sent")


def call_next_round():
    next()


def queue_cleaner(queue):
    for action in queue:

        if action.exec_round == main.current_party.round:
            action_in_execution = action.type

            action_in_execution(action)
        else:
            continue