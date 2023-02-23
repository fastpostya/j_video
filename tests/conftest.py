import pytest
import os
from utils.goods import Goods


@pytest.fixture()
def mouse():
    mouse = Goods("мышь Tech", 400, 5)
    return mouse

@pytest.fixture()
def keyboard():
    keyboard = Goods("клавиатура", 500, 0)
    return keyboard

@pytest.fixture()
def patf_csv_file():
    return os.sep.join(["tests", "items.csv"])

@pytest.mark.parametrize("goods", "str_goods",
            [(Goods("Ноутбук", 20000, 5), "Товар: Ноутбук, цена: 20000, количество: 5"),
            (Goods("Смартфон", 100, 1), "Товар: Смартфон, цена: 100, количество: 1"),
            (Goods("Ноутбук", 1000, 3), "Товар: Ноутбук, цена: 1000, количество: 3"),
            (Goods("Кабель", 10, 5), "Товар: Кабель, цена: 10, количество: 5"),
            (Goods("Мышка",  50, 5),"Товар: Мышка, цена: 50, количество: 5"),
            (Goods("Клавиатура", 75, 5), "Товар: Клавиатура, цена: 75, количество: 5 ")]
