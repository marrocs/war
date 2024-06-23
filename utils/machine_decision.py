import settings, logging
from .models import Action
from random import randint, choice
from math import floor

'''
A função abaixo deve receber a maquina como parametro, olhar seus atributos, analizar prioridades e retornar a decisão;
'''

logging.basicConfig(level=logging.INFO, encoding="utf-8", filename='./logs/party_info.log', format='%(asctime)s @ %(levelname)s @ %(message)s')
logging.basicConfig(level=logging.ERROR,encoding="utf-8", filename='./logs/party_error.log', format='%(asctime)s @ %(levelname)s @ %(message)s')

def machine_dismiss_military(player, mil_number):
    
    try:
        player.military -= mil_number
                
    except Exception as error:
        logging.error(f"Message: Malfunction at dismiss_military function; Name: {error.__name__}; Cause: {error.__cause__}; Traceback: {error.__traceback__}")        
        return "400 ERROR"
    
    else:
        return "200 OK"


def machine_movement_analyzer(machine):
    
    current_round = settings.current_party[0].round
    
    try:
        
        # Não tem civis o bastante, contratar civis
        if machine.civillian <= settings.MACHINE_MIN_CIVILLIANS:
                        
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

        # Tem o minimo de civis para movimentar economia mas pouco dinheiro: Investir     
        elif machine.money <= settings.MACHINE_MIN_MONEY:
            
            if machine.money <= 0:
                machine_dismiss_military(machine, machine.military)
                
            # Parametros (Executor, Target, Type, Quantity, ttl)
            quantity = randint(1, floor(machine.money))
                    
            # Instanciar objeto
            machine_action = Action(int(current_round), executor=machine, target=machine, type="invest", quantity=quantity, ttl=randint(1,10))
            
            machine.money -= quantity
            
            # Appendar na fila de execução
            settings.action_queue.append(machine_action)
            
            logging.info(f"ROUND {settings.current_party[0].round} - Player: {machine.name}, Action: {machine_action.type}, Succeded: Yes, Message: {machine.name} invested {quantity} for {machine_action.ttl} turns")
        
        # Tem Civil suficiente, tem dinheiro suficiente, mas não tem militar o bastante
        elif machine.military <= settings.MACHINE_MIN_MILITARY:
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

        # Se tem tudo, ataca
        else:                    
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
            
        
    
    except Exception as error:
        
            logging.info(f"ERROR: {error}")
            
            print("DEU RUIM")
            
            return "400 ERRO"
    
    else:
        
        return "200 OK"