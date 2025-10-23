import pytest
from calculator import Calculator

calc = Calculator()

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 5, 4),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert calc.add(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5),
    (9, 3, 3),
])
def test_divide(a, b, expected):
    assert calc.divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)

@pytest.mark.parametrize("n,expected", [
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (1, False),
    (0, False),
])
def test_is_prime_number(n, expected):
    assert calc.is_prime_number(n) == expected
