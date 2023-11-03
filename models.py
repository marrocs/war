party_id_counter = 0

class Party: 
    def __init__(self, players:list) -> None:
        self.id = party_id_counter
        self.players = [p for p in players]
        self.logs = []
        self.round = 0
        self.status = True  
        self.winner = ""

    def __repr__(self):
        return f"This party has: ID {self.id}, players: [{self.players}], logs: [{self.logs}], rounds: {self.round}, status: {self.status}, winner: {self.winner}"

    party_id_counter += 1

    
class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.money = 100
        self.military = 10

    def __repr__(self) -> str:
        return f'Player: {self.name}\nMoney:{self.money}\nMilitary: {self.military}'
    
    def show_infos(self) -> str:

        print(f'Your money: {self.money}\nYour military: {self.military}')
        
        return None


class Action:
    def __init__(self, round, executor, target, type:str, quantity, ttl:int) -> None:
        self.id = id
        self.round = round
        self.executor = executor
        self.target = target
        self.type = type
        self.quantity = quantity
        self.ttl = ttl
        self.exec_round = int(self.round) + int(self.ttl)


# class Unity:
#     # The minimal entity on game. Must hold health,

#     def __init__(self, id, tipo, saude, posicao) -> None:
#         pass

# class Civilian:
#     def __init__(self) -> None:
#         pass


# class Military:
#     def __init__(self) -> None:
#         pass


# class Infrastructure:
#     def __init__(self) -> None:
#         pass




