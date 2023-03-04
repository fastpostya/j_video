import pytest
import os
from utils.goods import Goods, Phone
from utils.keyboard import KeyBoard, Mixin


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


@pytest.fixture()
def phone_i():
    return Phone("I am phone", 15000, 5, 4)


@pytest.fixture()
def keyboard_test():
    return KeyBoard("Tech", 1500, 5)


@pytest.fixture()
def mixin_test():
    return Mixin('EN')
