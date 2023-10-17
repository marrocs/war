class Party:
    def __init__(self, player1, player2) -> None:
        pass
    

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
    def __init__(self, id, executor, target) -> None:
        pass

