import pytest
import pytest_cov
from utils.goods import Goods


def test_calculate_amount(mouse, keyboard):
    assert mouse.calculate_amount() == 2000
    item1 = Goods("name", 50, 2)
    assert keyboard.calculate_amount() == 0
    assert item1.calculate_amount() == 100


def test_apply_discount(mouse):
    assert mouse.pay_rate == 1
    item1 = Goods("name", 50, 2)
    item1.pay_rate = 0.8
    assert item1.apply_discount() is None
    assert item1.price == 40
    assert int(item1.calculate_amount()) == 80


def test__repr__(mouse, keyboard):
    assert str(mouse) == "Goods(name=мышь Tech, price=400, quantity=5)"
    assert str(keyboard) == "Goods(name=клавиатура Tech, price=500, quantity=0)"
