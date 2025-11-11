from calculator_logic import add, subtract, multiply, divide


# Tesing the addition logic
def test_add():
    assert add(3, 2) == 5
    assert add(3, 5) == 8
    assert add(10, 5) == 15


# Tesing the substraction logic
def test_subtract():
    assert subtract(2, 1) == 1
    assert subtract(5, 2) == 3
    assert subtract(10, 5) == 5


# Testing the multiplication logic
def test_multiply():
    assert multiply(2, 2) == 4
    assert multiply(3, 3) == 9
    assert multiply(5, 5) == 25


# Testing the division logic
def test_divide():
    assert divide(10, 5) == 2
    assert divide(5, 2) == 2.5
    assert divide(2.5, 0) == "Cant divide by 0"
