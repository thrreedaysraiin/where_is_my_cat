from abc import ABC, abstractmethod
from card import Cards
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0


class Player(ABC):
    def __init__(self):
        print('Player init')

    @abstractmethod
    def choose_card(self):
        pass

class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.score = 0
    def choose_card(self, cards, card, win_card):
        if card == win_card:
            self.score += 1
            return True
        else:
            return False








