class Party: 
    def __init__(self, players:list) -> None:
        self.id = 0
        self.players = [p for p in players]
        self.logs = []
        self.round = 0
        self.status = True
        

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.money = 100
        self.military = 10

    def __repr__(self) -> str:
        return f'Player: {self.name}\nMoney:{self.money}\nMilitary: {self.military}'
    
    def show_infos(self) -> str:
        return f'Your money: {self.money}\nYour military: {self.military}'

class Unity:
    # The minimal entity on game. Must hold health,

    def __init__(self, id, tipo, saude, posicao) -> None:
        pass

class Civilian:
    def __init__(self) -> None:
        pass

class Military:
    def __init__(self) -> None:
        pass

class Infrastructure:
    def __init__(self) -> None:
        pass

class Action:
    def __init__(self, round, executor, target, type:str, quantity, ttl:int) -> None:
        self.id = id
        self.round = round
        self.executor = executor
        self.target = target
        self.type = type
        self.quantity = quantity
        self.ttl = ttl
        self.expire = self.round + self.ttl


