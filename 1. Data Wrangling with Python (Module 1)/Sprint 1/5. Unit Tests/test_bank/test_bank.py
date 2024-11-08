from bank import value


def test_value():
    assert value("Hooba booba") == 20
    assert value("Hello") == 0
    assert value("Sup") == 100
