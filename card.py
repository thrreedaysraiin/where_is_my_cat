from cube import CatCube
class CardDeck:
    def __init__(self):
        self.cards = []
        self.create_cards()

    def create_cards(self):
        "Создает карты"
        cat_game = CatCube()
        for _ in range(27):
            cat_game.roll_cubes()
            card = CatCube()
            self.cards.append(card)

    def take_card(self):
        "Удаляет карту, когда игрок забиарет себе"
        if self.cards:
            return self.cards.pop()
        else:
            return None

    def __repr__(self):
        return f"CardDeck(cards={self.cards})"