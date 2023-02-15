import pytest
import pytest_cov
from utils.goods import Goods


def test_calculate_amount(mouse):
    assert mouse.calculate_amount() == 2000
    item = Goods("name", 50, 2)
    assert item.calculate_amount() == 100

def test_apply_discount(mouse):
    mouse.pay_rate = 0.8
    mouse.apply_discount()
    assert mouse.calculate_amount() == 0.8 * 2000.0
