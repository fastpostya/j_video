import pytest
from utils.goods import Phone


def test_add_item(phone_i,  mouse):
    assert phone_i.add_item(phone_i, mouse) == 10


def test__init__():
    assert Phone("iPhone 14", 120_000, 5, 2).name == "iPhone 14"
    with pytest.raises(ValueError):
        Phone("I am phone", 15000, 5, 0)


def test__repr__(phone_i) -> str:
    assert repr(phone_i) == "Phone(_Goods__name=I am phone, price=15000, quantity=5, _number_of_sim=4, name=I am phone)"


def test__str__(phone_i) -> str:
    assert str(phone_i) == "Телефон: I am phone, цена: 15000, количество: 5, количество сим-карт: 4"


def test_number_of_sim(phone_i):
    assert phone_i.number_of_sim == 4
    with pytest.raises(ValueError):
        phone_i.number_of_sim == 0

