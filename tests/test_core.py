import math
import pytest
from pulkit_calculator import add, sub, mul, div, pow, mod, floordiv

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_sub():
    assert sub(5, 2) == 3
    assert sub(0, 3) == -3

def test_mul():
    assert mul(3, 4) == 12
    assert mul(-2, 3) == -6

def test_pow():
    assert pow(2, 3) == 8
    assert pow(9, 0.5) == 3

def test_mod():
    assert mod(10, 3) == 1
    with pytest.raises(ZeroDivisionError):
        mod(1, 0)

def test_floordiv():
    assert floordiv(7, 2) == 3
    assert floordiv(8, 2) == 4

def test_div():
    assert div(10, 2) == 5
    assert math.isclose(div(7, 2), 3.5)

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)
