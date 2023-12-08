import random

class CatCube:
    def __init__(self):
        self.cat_colors = ["Белый", "Серый", "Рыжий"]   #кубик "цвет"
        self.cat_actions = ["Сидит", "Лежит", "Стоит"]   #кубик "что делает"
        self.cat_spots = ["Однотонный", "Полосатый", "Пятнистый"]  #кубик с пятнистотью кота

        self.roll_cubes()

    def roll_cubes(self):
        self.cat_color = random.choice(self.cat_colors)
        self.cat_action = random.choice(self.cat_actions)
        self.cat_spot = random.choice(self.cat_spots)

    def __repr__(self):
        return f"CatCube(cat_color={self.cat_color}, cat_action={self.cat_action}, cat_spot={self.cat_spot})"
