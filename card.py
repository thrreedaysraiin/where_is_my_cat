from cube import CatCube

class Cards:
    def __init__(self):
        self.cat_cards = []
    def set_up_game(self):
        # Создаем 27 карт с котами и добавляем их в игру
        cat1 = CatCube("Белый", "Лежит", "Полосатый")
        cat2 = CatCube("Рыжий", "Сидит", "Пятнистый")
        cat3 = CatCube("Белый", "Cтоит", "Пятнистый")
        cat4 = CatCube("Серый", "Лежит", "Полосатый")
        cat5 = CatCube("Рыжий", "Стоит", "Полосатый")
        cat6 = CatCube("Белый", "Лежит", "Однотонный")
        cat7 = CatCube("Серый", "Сидит", "Однотонный")
        cat8 = CatCube("Серый", "Сидит", "Пятнистый")
        cat9 = CatCube("Белый", "Стоит", "Однотонный")
        cat10 = CatCube("Серый", "Сидит", "Полосатый")
        cat11 = CatCube("Серый", "Стоит", "Пятнистый")
        cat12 = CatCube("Рыжий", "Сидит", "Однотонный")
        cat13 = CatCube("Серый", "Лежит", "Пятнистый")
        cat14 = CatCube("Белый", "Лежит", "Пятнистый")
        cat15 = CatCube("Серый", "Стоит", "Однотонный")
        cat16 = CatCube("Рыжий", "Лежит", "Пятнистый")
        cat17 = CatCube("Рыжий", "Лежит", "Однотонный")
        cat18 = CatCube("Белый", "Сидит", "Полосатый")
        cat19 = CatCube("Белый", "Стоит", "Полосатый")
        cat20 = CatCube("Рыжий", "Сидит", "Полосатый")
        cat21 = CatCube("Рыжий", "Стоит", "Пятнистый")
        cat22 = CatCube("Рыжий", "Лежит", "Полосатый")
        cat23 = CatCube("Белый", "Сидит", "Однотонный")
        cat24 = CatCube("Серый", "Лежит", "Однотонный")
        cat25 = CatCube("Серый", "Стоит", "Полосатый")
        cat26 = CatCube("Рыжий", "Стоит", "Однотонный")
        cat27 = CatCube("Белый", "Сидит", "Пятнистый")

        # Добавляем каждую карту в список карт игры
        self.cat_cards.extend([cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8, cat9, cat10, cat11, cat12,
                               cat13, cat14, cat15, cat16, cat17, cat18, cat19, cat20, cat21, cat22, cat23,
                               cat24, cat25, cat26, cat27])

    def __repr__(self):
        return f"CardDeck(cards={self.cat_cards})"