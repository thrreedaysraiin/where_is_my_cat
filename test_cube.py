import pytest
from cube import CatCube
def test_roll_cubes():
    cube = CatCube()
    cube.roll_cubes()
    assert cube.cat_color in cube.cat_colors
    assert cube.cat_action in cube.cat_actions
    assert cube.cat_spot in cube.cat_spots
def test_invalid_color():
    with pytest.raises(ValueError):
        cube = CatCube("Желтый", "Сидит", "Однотонный")

def test_invalid_action():
    with pytest.raises(ValueError):
        cube = CatCube("Белый", "Летит", "Однотонный")

def test_invalid_spot():
    with pytest.raises(ValueError):
        cube = CatCube("Белый", "Сидит", "Разноцветный")