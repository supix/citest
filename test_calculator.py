from main import Calculator

def test_double():
    d = Calculator()
    assert d.double(3) == 6

def test_multiply():
    d = Calculator()
    assert d.multiply(3, 5) == 15
