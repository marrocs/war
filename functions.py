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

    action = input('Your choice: ')

    # Invest
    if action == 1:
        invest_money(player)
    # Hire
    if action == 2:
        hire_military(player)
    # Atack
    if action == 3:
        attack_enemy(player)
    # Pass
    if action == 4:
        call_next_round()


    return None


def invest_money(player):
    quantity_to_invest = input("How much to invest?")
    investment_time = input("How many turn money should be invested?")

    if quantity_to_invest > player.money:
        print("You don't have all that. Try again.")
        invest_money(player)

    else:
        invest_action = Action(main.current_party.round, executor=player, target=player, type="invest", quantity=quantity_to_invest, ttl=investment_time)

        main.action_queue(invest_action)

        print(f'You have invested ${quantity_to_invest}!')

    return None


def hire_military(player):
    pass

def attack_enemy(player):
    pass

def call_next_round():
    pass
