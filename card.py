from cube import CatCube
class Cards:
    def __init__(self):
        self.cat_cards = ['n' for i in range(28)]
        self.cat = CatCube()

    def set_up_game(self):
        k = 0
        for color in self.cat.cat_colors:
            for actions in self.cat.cat_actions:
                for spots in self.cat.cat_spots:
                    self.cat_cards[k] = [color, actions, spots]
                    k += 1
        self.cat_cards[-1] = ['Карта-выручалка']
        print(self.cat_cards)
    def remove_card(self,card):
        self.cat_cards.remove(card)

        # Создаем 27 карт с котами и добавляем их в игру
    def __repr__(self):
        return f"CardDeck(cards={self.cat_cards})"
a = Cards()
a.set_up_game()
