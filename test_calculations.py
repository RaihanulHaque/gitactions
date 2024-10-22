from api.calculations import add, multiply, divide

def test_add():
    assert add(1, 2) == 3

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(5, 0) == "You can't divide by zero!?"