from adder import add


def test_add():
    assert add(1, 2) == 3


def test_add_minus():
    assert add(3, -4) == -1
