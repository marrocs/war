'''
TODO: Implementar uma forma de verificar se o usuario escolhido para ser atacado existe
'''
from utils.models import *
import settings, logging, sys
from math import floor
from random import choice, randint

#logging.basicConfig(level=logging.INFO, encoding="utf-8", filename=f'../logs/party_info.log', format='%(asctime)s @ %(levelname)s @ %(message)s')
logging.basicConfig(level=logging.ERROR,encoding="utf-8", filename=f'./logs/party_error.log', format='%(asctime)s @ %(levelname)s @ %(message)s')

# Uso: logging.info / logging.warning / logging.error


def receive_guests() -> str:

    try:
        guests_names = []

        num_players = int(input("How many players? "))
        
        
        if num_players == 1 or num_players == 0:            
            npc_number = int(input("How many NPCs?\n")) 

            print(f"\nThere will be {num_players} player and {npc_number} NPC's \n") # Problem here. Further code don't get executed
            

            for npc in range(npc_number):
                guests_names.append(f"machine_"+ str(npc))
 
        
        else:    

            print(f"\nThere will be {num_players} players \n")


        for x in range(num_players):

            name = input(f"Player's {x+1} name: ")
            guests_names.append(name)
            print(f"Player {name} registered for party")
            
            
        # Instantiate Players with names and Append Players to settings.players_list

        for p in guests_names:
            new_player = Player(p)

            settings.players_list.append(new_player)         
    
    except Exception as error:
        
        logging.error(f"Message: Malfunction at receive_guests function; Name: {error.__name__}; Cause: {error.__cause__}; Traceback: {error.__traceback__}")

        return f"400 ERROR"

    
    else:
        return "200 OK"


def create_party(players_list) -> list:

    try:
        
        new_party = Party(players_list)
        
        settings.current_party.append(new_party) 

        print(f'Party nº {settings.current_party[0].id} initiated with: {settings.current_party[0].players}')

        logging.info(f'Party nº {settings.current_party[0].id} initiated with: {settings.current_party[0].players}')

    except Exception as error:
        logging.error(f"Message: Malfunction at create_party function; Name: {error.__name__}; Cause: {error.__cause__}; Traceback: {error.__traceback__}")        
        return "400 ERROR"
    
    return "200 OK"
        

def menu_action(player) -> str:

    try:
        print(f'''

    <<----->> MENU ACTION <<----->
                ROUND {settings.current_party[0].round}

Player: {player.name}   |   Money: {player.money}   |   Army: {player.military}
*****************************************    
*                                       *
*                                       *
*    1 - Invest    2 - Hire military    *     
*                                       *
*    3 - Attack    4 - Pass             *
*                                       *
*                                       *
*****************************************
    ''')


        action = input('\n\n\nYour choice: ')

    except Exception as error:

        logging.error(f"Message: Malfunction at menu_action function; Name: {error.__name__}; Cause: {error.__cause__}; Traceback: {error.__traceback__}")        

        return "400 ERROR"

    else:

        return f"200 {action}"


def get_action(player, return_code) -> str:

    try:
        splited_return_code = return_code.split(' ')
        action = int(splited_return_code[1])
        current_round = int(settings.current_party[0].round)


        # Invest
        if action == 1:

            quantity_to_invest = input("How much to invest?")

            while int(quantity_to_invest) > int(player.money):
                
                print("You don't have all that. Try again.")
                #quantity_to_invest = input("How much to invest?")

                logging.info(f"ROUND {settings.current_party[0].round} - Player: {player.name}, Action: invest, Succeded: No, Message: Player dont have that money")

                return "400 ERROR"

            else:

                investment_time = input("How many turns money should be invested?")

                invest_action = Action(current_round, executor=player, target=player, type="invest", quantity=quantity_to_invest, ttl=investment_time)
                settings.action_queue.append(invest_action)
                player.money -= int(quantity_to_invest)

                print(f'You have invested ${quantity_to_invest}!')

                logging.info(f"ROUND {settings.current_party[0].round} - Player: {player.name}, Action: {invest_action.type}, Succeded: Yes, Message: {invest_action.executor} invested {invest_action.quantity} for {invest_action.ttl} turns. Expect return in round {int(settings.current_party[0].round) + int(invest_action.ttl) + 1}")

                return "200 OK"
            
        # Hire
        elif action == 2:

            quantity_to_hire = input("how many soldiers to hire?")
            price = int(quantity_to_hire) * 2

            while price > int(player.money):

                print("You don't have all that. Try again.")

                logging.info(f"ROUND {settings.current_party[0].round} - Player: {player.name}, Action: Hire, Succeded: No, Message: {player.name} tried to order more soldiers that can afford")

                return "400 ERROR"

            else:

                hire_action = Action(current_round, executor=player, target=player, type="hire", quantity=quantity_to_hire, ttl=2)
                settings.action_queue.append(hire_action)
                player.money -= price

                print(f'You have asked for {quantity_to_hire} soldiers that should be delivered in round {int(settings.current_party[0].round) + int(hire_action.ttl) + 1} !')

                logging.info(f"ROUND {settings.current_party[0].round} - Player: {player.name}, Action: {hire_action.type}, Succeded: Yes, Message: {hire_action.executor.name} ordered {quantity_to_hire} soldiers")

                return "200 OK"

        # Attack
        elif action == 3:


            print("These are the other players: \n\n")
                    
            for x in settings.players_list:

                if x.name == player.name:

                    pass
                
                else:
                    print(x.name)

            target_name = input("Who do you want attack?")
            
            target_player = 0

            for x in settings.players_list:
                if x.name == target_name:
                    target_player = x


            while target_player == player:

                print("You can't attack yourself")

                logging.info(f"ROUND {settings.current_party[0].round} - Player: {player.name}, Action: {action}, Succeded: No, Message: {player.name} tried to attack himself")
                
                return "400 ERROR"

            else:

                force_employed = input("\n\nHow many soldiers will be deployed?")

                while int(player.military) < int(force_employed):

                    print("You don't have all that. Try again.")

                    logging.info(f"ROUND {settings.current_party[0].round} - Player: {player.name}, Action: {action}, Succeded: No, Message: {player.name} tried to use more soldiers than got")
                    
                    return "400 ERROR"

                else:

                    attack_action = Action(current_round, executor=player, target=target_player, type="attack", quantity=force_employed, ttl=2)
                    settings.action_queue.append(attack_action)
                    print(f'You sent {force_employed} soldiers to attack {attack_action.target}!')

                    player.military -= int(force_employed)

                    logging.info(f"ROUND {settings.current_party[0].round} - Player: {player.name}, Action: {action}, Succeded: Yes, Message: {attack_action.target.name} will be hit by {attack_action.quantity} {player.name}'s soldiers at round {(settings.current_party[0].round) + attack_action.ttl + 1}!")

                    return "200,OK"
                
        # Pass
        elif action == str(4):
            return "200 OK"
    
    except Exception as error:
        logging.error(f"Message: Malfunction at get_action function; Name: {error.__name__}; Cause: {error.__cause__}; Traceback: {error.__traceback__}")        

        return "400 ERROR"
        
    else:
        return "200 OK"                   


def invest(action):

    try:
        invested_value = action.quantity
        interest_rate = settings.INTEREST_RATE
        time_investment = action.ttl
        investment_return = floor((invested_value * time_investment * (interest_rate*100))/100)

        action.executor.money += investment_return
                    
        print(f'{action.executor} just received ${investment_return} back!')


        logging.info(f"ROUND {settings.current_party[0].round} - Player: {action.executor.name}, Action: {action.type}, Succeded: Yes, Message: {action.executor.name} received ${investment_return} back")
    
    except Exception as error:
        logging.error(f"Message: Malfunction at invest function; Name: {error.__name__}; Cause: {error.__cause__}; Traceback: {error.__traceback__}")        
        return "400 ERROR"
    
    else:    
        return "200 OK"


def hire_military(action):

    try:
        quantity_to_hire = int(action.quantity)

        action.executor.military += quantity_to_hire
        print(f"Good news, {action.executor.name}. The {quantity_to_hire} soldiers you requested has arrived.")


        logging.info(f"ROUND {settings.current_party[0].round} - Player: {action.executor.name}, Action: {action.type}, Succeded: Yes, Message: {action.executor.name} received {quantity_to_hire} soldiers")

    except Exception as error:
        logging.error(f"Message: Malfunction at hire function; Name: {error.__name__}; Cause: {error.__cause__}; Traceback: {error.__traceback__}")        
        return "400 ERROR"
    
    else:
        return "200 OK"


def hire_civillian(action):

    try:
        quantity_to_hire = int(action.quantity)

        action.executor.civillian += quantity_to_hire
        print(f"Good news, {action.executor.name}. The {quantity_to_hire} civillian you requested has arrived.")


        logging.info(f"ROUND {settings.current_party[0].round} - Player: {action.executor.name}, Action: {action.type}, Succeded: Yes, Message: {action.executor.name} received {quantity_to_hire} civillian")

    except Exception as error:
        logging.error(f"Message: Malfunction at hire function; Name: {error.__name__}; Cause: {error.__cause__}; Traceback: {error.__traceback__}")        
        return "400 ERROR"
    
    else:
        return "200 OK"


def attack(action):
    
    try:
        offensive_player = action.executor
        defensive_player = action.target
        offensive_force = int(action.quantity)
        defensive_force = int(action.target.military)
        defensive_civillians = int(action.target.civillian)

        print(f"Player's {offensive_player} attack {defensive_player} with {offensive_force} soldiers. ")
        logging.info(f"ROUND {settings.current_party[0].round} - Player: {offensive_player}, Action: {action.type}, Succeded: Yes, Message: Player's {offensive_player} is attacking {defensive_player} with {offensive_force} soldiers.")

        print(f"""
    ***************************************************
                                                    
    {offensive_player}  {offensive_force}  X  {defensive_force}  {defensive_player}
                                                    
    ***************************************************
    """)

    
        if defensive_force <= 0:
            
            civillian_loss = floor((offensive_force * ((settings.CIVILIAN_INJURY_RATE)*100))/100)
            
            
            print(f"{defensive_player} has no soldiers to defend itself")
            
            if civillian_loss > defensive_civillians:
            
                print(f"ENDGAME for {defensive_player}")
                end_party_for_player(defensive_player)

                logging.info(f"ROUND {settings.current_party[0].round} - Player: {action.executor.name}, Action: {action.type}, Succeded: Yes, Message: ENDGAME for {defensive_player}")
                
            elif civillian_loss == defensive_civillians:
                
                defensive_player.civillian = 0
                end_party_for_player(defensive_player)
                
            else:
                
                defensive_player.civillian -= civillian_loss
                

        else:
            
            # atacante em maior numero
            if int(offensive_force) > int(defensive_force):
                                
                offensive_survivals = int(offensive_force) - int(defensive_force)

                action.target.military = 0
                action.executor.military += offensive_survivals
                
                print(f"TESTE: o numero de soldados de {action.target} deveria ser 0 e é {action.target.military}")
                print(f"{offensive_survivals} {offensive_player.name}'s soldiers survived and {action.target.name} lost all it's soldiers")

                logging.info(f"ROUND {settings.current_party[0].round} - Player: {action.executor.name}, Action: {action.type}, Succeded: Yes, Message: {action.executor.name} attack {action.target.name} and WIN")

            # atacante em menor numero
            elif int(offensive_force) < int(defensive_force):
                
                defensive_survivals = int(defensive_force) - int(offensive_force)
                defensive_player.military = defensive_survivals

                print(f"{defensive_force - offensive_force} {defensive_player.name}'s soldiers survived and {action.executor.name} lost all it's soldiers")

                logging.info(f"ROUND {settings.current_party[0].round} - Player: {action.executor.name}, Action: {action.type}, Succeded: No, Message: {action.executor.name} attack {action.target.name} and LOST.")

            # Forcas iguais
            elif offensive_force == defensive_force:
                
                defensive_player.military, offensive_player.military = 0, 0
                print(f"{offensive_force - defensive_force}") 
                print(f"{offensive_player.name} LOST the battle")
                
                logging.info(f"ROUND {settings.current_party[0].round} - Player: {action.executor.name}, Action: {action.type}, Succeded: No, Message: {action.executor.name} attack {action.target.name} and LOST.")


            else:
                raise ValueError("offensive_force and defensive_force are not different neither equal. Go check that weird shit.")

    except Exception as error:

        except_type, except_object, except_traceback = sys.exc_info()

        logging.error(f"Message: Malfunction at attack function; Name: {error.__name__}; Cause: {error.__cause__}; Traceback: {error.__traceback__}")        
        return "400 ERROR"

    else:

        return "200 OK"


def parser(queue):  

    try:
        
        current_party = settings.current_party
        
        # Tarefa de limpar a fila de ações
        for action in queue:

            if action.exec_round == current_party[0].round:
                if action.executor in settings.players_list:
                    action_to_execute = globals().get(action.type)

                    action_to_execute(action)

                    logging.info(f"ROUND {settings.current_party[0].round} - QUEUE CLEANER: Player's {action.executor.name} action for {action.type} has been executed;")
                    settings.action_queue.remove(action)
                    return "200 OK"
                
                else:
                    queue.remove(action)
                    return "200 OK"

            else:
                #logging.info(f"QUEUE CLEANER: Round {settings.current_party[0].round} - Player's {action.executor.name} action for {action.type} should occour in round {action.exec_round}")
                pass


    except Exception as error:

        logging.error(f"Message: Malfunction at invest function; Name: {error.__name__}; Cause: {error.__cause__}; Traceback: {error.__traceback__}")        
        return "400 ERROR"

    else:

        return "200 OK"


def machine_movement(machine):
    
    try:
        current_round = settings.current_party[0].round
            
        # ----------------------------  Jeito facil - Aleatoriedade ----------------------
     
        # O npc deve sortear um número entre 1 e 5. A partir dai deve escrever a propria Action e appendar 
        
        # Sorteando primeira ação
        npc_action = randint(1,5)
        
        # Invest
        if npc_action == 1:
            
            if machine.money >= 1:
            
                # Parametros (Executor, Target, Type, Quantity, ttl)
                quantity = randint(1, floor(machine.money))
                        
                # Instanciar objeto
                machine_action = Action(int(current_round), executor=machine, target=machine, type="invest", quantity=quantity, ttl=randint(1,10))
                
                machine.money -= quantity
                
                # Appendar na fila de execução
                settings.action_queue.append(machine_action)
                
                logging.info(f"ROUND {settings.current_party[0].round} - Player: {machine.name}, Action: {machine_action.type}, Succeded: Yes, Message: {machine.name} invested {quantity} for {machine_action.ttl} turns")
            
                
                return "200 OK"
            
            else:
                
                machine_movement(machine)
                
            return "200 OK"
        
        # Hire military
        elif npc_action == 2:
            
            military_price = settings.MILITARY_PRICE
            maximum_military_player_can_buy=floor(machine.money/military_price)
            quantity = randint(1, maximum_military_player_can_buy)  # TODO: 
            
            if quantity <= maximum_military_player_can_buy:                 
                
                # Instanciar objeto
                machine_action = Action(current_round, executor=machine, target=machine, type="hire_military", quantity=quantity, ttl=2)
                
                machine.money -= (quantity*military_price)
                
                # Appendar na fila de execução
                settings.action_queue.append(machine_action)
                
                logging.info(f"ROUND {settings.current_party[0].round} - Player: {machine.name}, Action: {machine_action.type}, Succeded: Yes, Message: {machine.name} ordered {quantity} soldiers")

            else:
                machine_movement(machine)
                
                
            return "200 OK"
        
        # Hire civillian
        elif npc_action == 3:
            
            civillian_price = settings.CIVILLIAN_PRICE
            maximum_civillian_player_can_buy=floor(machine.money/civillian_price)
            quantity = randint(1, maximum_civillian_player_can_buy)  
            
            if quantity <= maximum_civillian_player_can_buy:                
                
                # Instanciar objeto
                machine_action = Action(current_round, executor=machine, target=machine, type="hire_civillian", quantity=quantity, ttl=2)
                
                machine.money -= (quantity*civillian_price)
                
                # Appendar na fila de execução
                settings.action_queue.append(machine_action)
                
                logging.info(f"ROUND {settings.current_party[0].round} - Player: {machine.name}, Action: {machine_action.type}, Succeded: Yes, Message: {machine.name} ordered {quantity} soldiers")

            else:
                machine_movement(machine)
                
                
            return "200 OK"
        
        # Attack
        elif npc_action == 4:
            
            # Parametros (Executor, Target, Type, Quantity, ttl)
            target = choice(settings.players_list)
            
            while target.name == machine.name:
                target = choice(settings.players_list)

            if machine.military >= 1:
            
                quantity = randint(1, (machine.military + 1))
                
                if quantity <= machine.military:
                
                    # Instanciar objeto
                    machine_action = Action(current_round, executor=machine, target=target, type="attack", quantity=quantity, ttl=2)
                    
                    machine.military -= quantity
                    
                    # Appendar na fila de execução
                    settings.action_queue.append(machine_action)
                    
                    logging.info(f"ROUND {settings.current_party[0].round} - Player: {machine.name}, Action: {machine_action.type}, Succeded: Yes, Message: {machine.name} sent {quantity} units to attack {target.name}. Action should happen in round {machine_action.order_round + machine_action.ttl}")
                
                    
                    return "200 OK"
                
                else:
                    
                    print("TESTE: TA TENTANDO ATACAR COM MAIS SOLDADOS DO QUE TEM")
            
            else:
                    logging.info(f"ROUND {settings.current_party[0].round} - Player: {machine.name}, Action: attack, Succeded: No, Message: {machine.name} has no soldiers to attack")

                    return "200 OK"
            
        # Pass
        elif npc_action == 5:        
            logging.info(f"ROUND {settings.current_party[0].round} - Player: {machine.name}, Action: pass")
        
        # Erro
        else:
            
            logging.info(f"ERROR: primeira ação do NPC deu erro. Sorteou numero invalido")
            
            return "400 ERRO"
            
            
            
        # ----------------------------  Jeito dificil - Inteligencia simples ----------------------
        #machine_decision.


    except Exception as error:
        logging.error(f"Message: Malfunction at machine_movement function; Traceback: {error.__traceback__}")        
        return "400 ERROR"
    
    else:
        
        return "200 OK"


def bill_atributes(players):
    
    try:
        
        for p in players:
            
            # <--------------------------------------------------------------------->
            # Update revenue produced by civillians
            civillian_produtivity = settings.CIVILIAN_PRODUCTIVITY
            revenue = floor((p.civillian * (civillian_produtivity*100))/100)
            p.money += revenue
            
                
            # <--------------------------------------------------------------------->
            # Charge for military maintance
            military_maintance = settings.MILITARY_MAINTANCE
            military_bill = floor((p.military*(military_maintance*100))/100)
            
            p.money -= military_bill         
            
    except Exception as error:
        logging.error(f"Message: Malfunction at invest function; Name: {error.__name__}; Cause: {error.__cause__}; Traceback: {error.__traceback__}")        
        return "400 ERROR"
    
    else:
        return "200 OK"
    
       
def shut_party(party):
    
    try:
        settings.action_queue.clear()
        settings.current_party[0].status = False
        logging.info(f"{party.winner} WINS the game")
        print(f"{settings.current_party[0].winner} WINS THE PARTY")
        
        
    except Exception as error:
        
        logging.error(f"Message: Malfunction at invest function; Name: {error.__name__}; Cause: {error.__cause__}; Traceback: {error.__traceback__}")        
        return "400 ERROR"
    
    return "200 OK"


def end_party_for_player(player):
    
    # Pop loser player from settings.players_list
    for u in settings.players_list:
        if u.name == player.name:
            settings.players_list.remove(u)
            logging.info(f"ROUND {settings.current_party[0].round} - ADMIN: {u.name} removed from players list")
            
            for action in settings.action_queue:
                
                if action.executor == player.name or action.target == player.name:
                    
                    settings.action_queue.remove(action)
                    
                    logging.info(f"ADMIN: all {u.name} actions was cleared")
            
