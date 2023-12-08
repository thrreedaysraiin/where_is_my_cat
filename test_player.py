import pytest
from player import HumanPlayer
def test_choose_card():
    human = HumanPlayer('Taehyung')
    assert human.choose_card(['Белый', 'Сидит', 'Однотонный'], ['Белый', 'Сидит', 'Однотонный']) == True

    human = HumanPlayer('Jungkook')
    assert human.choose_card(['Белый', 'Сидит', 'Однотонный'], ['Рыжий', 'Лежит', 'Полосатый']) == False

    human = HumanPlayer('Jimin')
    human.choose_card(['Белый', 'Сидит', 'Однотонный'], ['Белый', 'Сидит', 'Однотонный'])
    assert human.score == 1

    human = HumanPlayer('Namjoon')
    human.choose_card(['Белый', 'Сидит', 'Однотонный'], ['Серый', 'Сидит', 'Полосатый'])
    assert human.score == 0



