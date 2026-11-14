from bank import calculate_balance

def test_calculate_balance():
    assert calculate_balance(100000, 50000, 20000) == 130000

def test_zero_deposit():
    assert calculate_balance(100000, 0, 20000) == 80000

