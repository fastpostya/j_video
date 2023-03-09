import pytest
import pytest_cov
from utils.goods import Goods
from utils.csverror import InstantiateCSVError


def test__init__(mouse: Goods):
    assert mouse._Goods__name == "мышь Tech"
    assert mouse.price == 400
    assert mouse.quantity == 5
    with pytest.raises(NameError, match="Длина названия товара не должна превышать 10 символов!"):
        item = Goods("очень длинное имя", 1, 1)


def test_calculate_amount(mouse: Goods, keyboard: Goods):
    assert mouse.calculate_amount() == 2000
    item1 = Goods("name", 50, 2)
    assert item1.calculate_amount() == 100
    assert keyboard.calculate_amount() == 0


def test_apply_discount(mouse: Goods):
    assert mouse.pay_rate == 1
    item1 = Goods("name", 50, 2)
    item1.pay_rate = 0.8
    assert item1.apply_discount() == 40
    assert item1.price == 40
    assert int(item1.calculate_amount()) == 80


def test__repr__():
    assert repr(Goods("Ноутбук", 20000, 5)) == \
        "Goods(_Goods__name=Ноутбук, price=20000, quantity=5)"
    assert repr(Goods("Смартфон", 100, 1)) == \
        "Goods(_Goods__name=Смартфон, price=100, quantity=1)"


def test_is_integer() -> bool:
    item = Goods("name", 50, 2)
    assert item.is_integer(5) is True
    assert item.is_integer(5.0) is True
    assert item.is_integer(5.5) is False
    assert item.is_integer("5") is False


def test_load_from_csv(patf_csv_file: str) -> list:
    """файл существует, все столбцы присутствуют"""
    item = Goods("name", 50, 2)
    assert len(item.load_from_csv(patf_csv_file)) == 5
    assert isinstance(item.load_from_csv(patf_csv_file)[0], Goods)
    assert repr(item.load_from_csv(patf_csv_file)[0]) == "Goods(_Goods__name=Смартфон, price=100, quantity=1)"


def test_load_from_csv_no_file(mouse: Goods):
    """файл отсутствует по указанному пути"""
    with pytest.raises(FileNotFoundError):
        mouse.load_from_csv("")


def test_load_from_csv_no_fieldnames(wrong_csv_file, mouse: Goods):
    """файл существует, нет столбца"""
    with pytest.raises(InstantiateCSVError):
        mouse.load_from_csv(wrong_csv_file)


def test__str__():
    assert str(Goods("Ноутбук", 20000, 5)) == \
        "Товар: Ноутбук, цена: 20000, количество: 5"
    assert str(Goods("Смартфон", 100, 1)) == \
        "Товар: Смартфон, цена: 100, количество: 1"
