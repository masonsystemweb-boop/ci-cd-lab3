import pytest
from app import add, subtract, multiply, divide, greet

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(6, 7) == 42

def test_divide():
    assert divide(8, 2) == 4
    with pytest.raises(ValueError):
        divide(1, 0)

def test_greet():
    assert greet("Gleb") == "Hello, Gleb!"
