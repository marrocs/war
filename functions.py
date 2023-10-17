
def party(player_1, player_2):

    round = 0
    party_is_on: True
    action_queue = []

    while party_is_on is True:
        # printar as infos de player 1

        print(player_1)

        menu_action()

        # Invest
        if menu_action == 1:
            pass
        # Hire
        if menu_action == 2:
            pass
        # Atack
        if menu_action == 3:
            pass
        # Pass
        if menu_action == 4:
            pass

        print(player_2)

        menu_action
        
        

def menu_action(player):
    print(f"Hello {player.name}")
    player.show_infos(player)
    
    print("You might: \n1-Invest\n2-Buy military\n3-Attack\n4-Pass")

    action = input('Your choice: ')

    return int(action)


def invest_money(player):
    quantity_to_invest = input("How much to invest?")

    if quantity_to_invest > player.money:
        print("You don't have all that")

    else:
        pass

def hire_military():
    pass

def attack():
    pass