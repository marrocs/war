'''
TODO: Implementar uma forma de verificar se o usuario escolhido para ser atacado existe
'''
from utils.models import *
import settings, logging, sys, traceback
from math import floor
from random import choice, randint
from time import sleep

logging.basicConfig(level=logging.INFO, encoding="utf-8", filename=f'./party_info.log', format='%(asctime)s @ %(levelname)s @ %(message)s')
logging.basicConfig(level=logging.ERROR,encoding="utf-8", filename=f'./party_error.log', format='%(asctime)s @ %(levelname)s @ %(message)s')

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
        interest_rate = 0.8
        time_investment = action.ttl
        investment_return = floor((float(invested_value) * float(time_investment) * float(interest_rate)))

        action.executor.money += investment_return
                    
        print(f'{action.executor} just received ${investment_return} back!')


        logging.info(f"ROUND {settings.current_party[0].round} - Player: {action.executor.name}, Action: {action.type}, Succeded: Yes, Message: {action.executor.name} received ${investment_return} back")
    
    except Exception as error:
        logging.error(f"Message: Malfunction at invest function; Name: {error.__name__}; Cause: {error.__cause__}; Traceback: {error.__traceback__}")        
        return "400 ERROR"
    
    else:    
        return "200 OK"


def hire(action):

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


def attack(action):
    
    try:
        offensive_player = action.executor
        defensive_player = action.target
        offensive_force = int(action.quantity)
        defensive_force = int(action.target.military)

        print(f"Player's {offensive_player} attack {defensive_player} with {offensive_force} soldiers. ")
        logging.info(f"ROUND {settings.current_party[0].round} - Player: {offensive_player}, Action: {action.type}, Succeded: Yes, Message: Player's {offensive_player} is attacking {defensive_player} with {offensive_force} soldiers.")

        print(f"""
    ***************************************************
                                                    
    {offensive_player}  {offensive_force}  X  {defensive_force}  {defensive_player}
                                                    
    ***************************************************
    """)

    
        if defensive_force <= 0:
            
            print(f"{defensive_player} has no soldiers and DIED")
            print(f"ENDGAME for {defensive_player}")

            logging.info(f"ROUND {settings.current_party[0].round} - Player: {action.executor.name}, Action: {action.type}, Succeded: Yes, Message: ENDGAME for {defensive_player}")


            # Pop loser player from settings.players_list
            for u in settings.players_list:
                if u.name == defensive_player.name:
                    settings.players_list.remove(u)
                    logging.info(f"ROUND {settings.current_party[0].round} - ADMIN: {u.name} removed from players list")
                    
                    for action in settings.action_queue:
                        
                        if action.executor == defensive_player.name or action.target == defensive_player.name:
                            
                            settings.action_queue.remove(action)
                            
                            logging.info(f"ADMIN: all {u.name} actions was cleared")
                    
            
            # Check if there are other players beyond offensive_player. If aint, shut party
            if len(settings.players_list) == 1:
                
                settings.current_party[0].winner = offensive_player.name

                settings.current_party[0].status = False
                
                return "200 OK"


        else:
            
            # atacante em maior numero
            if int(offensive_force) > int(defensive_force):
                                
                offensive_survivals = int(offensive_force) - int(defensive_force)

                action.target.military = 0
                action.executor.military += offensive_survivals
    
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


def queue_cleaner(queue):
    
    try:
        current_round = int(settings.current_party[0].round)

    
        for action in queue:

            if int(action.exec_round) == int(settings.current_party[0].round):
                if action.executor in settings.players_list:
                    action_to_execute = globals().get(action.type)

                    action_to_execute(action)

                    logging.info(f"ROUND {settings.current_party[0].round} - QUEUE CLEANER: Player's {action.executor.name} action for {action.type} has been executed;")
                    settings.action_queue.remove(action)
                
                else:
                    queue.remove(action)

            else:
                
                #logging.info(f"QUEUE CLEANER: Round {current_round} - Player's {action.executor.name} action for {action.type} should occour in round {action.exec_round}")
                pass

    except Exception as error:

        logging.error(f"Message: Malfunction at invest function; Name: {error.__name__}; Cause: {error.__cause__}; Traceback: {error.__traceback__}")        
        return "400 ERROR"

    else:

        return "200 OK"
    

def machine_movement(machine):
    
    try:
        current_round = int(settings.current_party[0].round)
        
        #sleep(0.1)

            
        # ----------------------------  Jeito facil - Aleatoriedade ----------------------
        
        
            # O npc deve sortear um número entre 1 e 4. A partir dai deve escrever a propria Action e appendar 
        
        # Sorteando primeira ação
        npc_action = randint(1,4)
        
        # Invest
        if npc_action == 1:
            
            if machine.money >= 1:
            
                # Parametros (Executor, Target, Type, Quantity, ttl)
                quantity = randint(1, (machine.money + 1))
                        
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
        
        # Hire
        elif npc_action == 2:
            
            if machine.money >= 2:
                # Parametros (Executor, Target, Type, Quantity, ttl)
                quantity = randint(1, floor(machine.money/2))  # TODO: 
                
                # Instanciar objeto
                machine_action = Action(current_round, executor=machine, target=machine, type="hire", quantity=quantity, ttl=2)
                
                machine.money -= quantity*2
                
                # Appendar na fila de execução
                settings.action_queue.append(machine_action)
                
                logging.info(f"ROUND {settings.current_party[0].round} - Player: {machine.name}, Action: {machine_action.type}, Succeded: Yes, Message: {machine.name} ordered {quantity} soldiers")

            else:
                machine_movement(machine)
                
                
            return "200 OK"
        
        # Attack
        elif npc_action == 3:
            
            if len(settings.players_list) <= 1:
                settings.current_party[0].status = False
            
            else:
            # Parametros (Executor, Target, Type, Quantity, ttl)
                target = choice(settings.players_list)
                
                while target.name == machine.name:
                    target = choice(settings.players_list)

                if machine.military >= 1:
                
                    quantity = randint(1, (machine.military + 1))
                    
                    # Instanciar objeto
                    machine_action = Action(current_round, executor=machine, target=target, type="attack", quantity=quantity, ttl=2)
                    
                    machine.military -= quantity
                    
                    # Appendar na fila de execução
                    settings.action_queue.append(machine_action)
                    
                    logging.info(f"ROUND {settings.current_party[0].round} - Player: {machine.name}, Action: {machine_action.type}, Succeded: Yes, Message: {machine.name} sent {quantity} units to attack {target.name}. Action should happen in round {machine_action.order_round + machine_action.ttl}")
                
                    
                    return "200 OK"
                
                else:
                    logging.info(f"ROUND {settings.current_party[0].round} - Player: {machine.name}, Action: attack, Succeded: No, Message: {machine.name} has no soldiers to attack")

                    return "200 OK"
            
        # Pass
        elif npc_action == 4:        
            logging.info(f"ROUND {settings.current_party[0].round} - Player: {machine.name}, Action: pass")
        
        
        else:
            
            logging.info(f"ERROR: primeira ação do NPC deu erro. Sorteou numero invalido")
            
            return "400 ERRO"
            
    except Exception as error:
        logging.error(f"Message: Malfunction at invest function; Name: {error.__name__}; Cause: {error.__cause__}; Traceback: {error.__traceback__}")        
        return "400 ERROR"
    
    else:
        
        return "200 OK"

       
def end_party(party):
    
    try:
        settings.action_queue.clear()
        logging.info(f"{party.winner} WINS the game")
        print(f"{settings.current_party[0].winner} WINS THE PARTY")
        
        
    except Exception as error:
        
        logging.error(f"Message: Malfunction at invest function; Name: {error.__name__}; Cause: {error.__cause__}; Traceback: {error.__traceback__}")        
        return "400 ERROR"
    
    return "200 OK"


# def imprimir_retangulo(num_caracteres):
#     # Calcula o número mais próximo de linhas e colunas para formar um retângulo aproximadamente quadrado
#     num_linhas = int(num_caracteres**0.5)
#     num_colunas = num_caracteres // num_linhas

#     # Imprime o retângulo
#     for _ in range(num_linhas):
#         print("*" * num_colunas)
        
