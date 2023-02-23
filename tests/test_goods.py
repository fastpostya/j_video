import pytest
#import pytest_cov
import utils
from utils.goods import Goods


def test__init__(mouse):
    assert mouse._Goods__name == "мышь Tech"
    assert mouse.price == 400
    assert mouse.quantity == 5
    with pytest.raises(NameError, match="Длина названия товара не должна превышать 10 символов!"):
        item = Goods("очень длинное имя", 1, 1 )


def test_calculate_amount(mouse, keyboard):
    assert mouse.calculate_amount() == 2000
    item1 = Goods("name", 50, 2)
    assert item1.calculate_amount() == 100
    assert keyboard.calculate_amount() == 0


def test_apply_discount(mouse):
    assert mouse.pay_rate == 1
    item1 = Goods("name", 50, 2)
    item1.pay_rate = 0.8
    assert item1.apply_discount() == 40
    assert item1.price == 40
    assert int(item1.calculate_amount()) == 80


def test__repr__(mouse):
    assert repr(mouse) == "Goods(_Goods__name=мышь Tech, price=400, quantity=5)"


def test_is_integer():
    item = Goods("name", 50, 2)
    assert item.is_integer(5) is True
    assert item.is_integer(5.0) is True
    assert item.is_integer(5.5) is False
    assert item.is_integer("5") is False


def test_load_from_csv(patf_csv_file) -> list:
    item = Goods("name", 50, 2)
    assert len(item.load_from_csv(patf_csv_file)) == 5
    assert isinstance(item.load_from_csv(patf_csv_file)[0], Goods)

def test__str__(self, goods, str_goods):
    assert str(self) == str_goods

