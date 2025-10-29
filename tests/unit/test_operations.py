import pytest
from app.operations import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(2.5, 3) == 5.5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(5.5, 2) == 3.5
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(2.5, 4) == 10.0
    assert multiply(0, 10) == 0

def test_divide():
    assert divide(6, 3) == 2.0
    assert divide(5.5, 2) == 2.75
    with pytest.raises(ValueError):
        divide(5, 0)
