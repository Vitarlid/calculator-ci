from calc import calculate

def test_addition():
    assert calculate(10, 5, 1) == 15

def test_subtraction():
    assert calculate(10, 5, 2) == 5

def test_division_by_zero():
    assert calculate(10, 0, 4) == "Cannot divide by zero"
