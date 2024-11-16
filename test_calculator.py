import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0


def test_divide(calc):
    assert calc.divide(6, 2) == 3
    assert calc.divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        calc.divide(10, 0)
