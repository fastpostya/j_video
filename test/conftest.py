import pytest
from utils.goods import Goods


@pytest.fixture()
def mouse():
    mouse = Goods("мышь Tech", 400, 5)

    return mouse