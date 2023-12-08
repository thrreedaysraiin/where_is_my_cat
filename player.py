from abc import ABC, abstractmethod
class Player(ABC):
    def __init__(self):
        print('Player init')

    @abstractmethod
    def choose_card(self, card, win_card):
        pass
class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.score = 0
    def choose_card(self, card, win_card):
        if card == win_card:
            self.score += 1
            return True
        else:
            return False








