from codding.Richest import maximumWealth


def test_maximumWealth_1():
    assert maximumWealth([[1, 2, 3], [3, 2, 1]]) == 6


def test_maximumWealth_2():
    assert maximumWealth([[1, 5], [7, 3], [3, 5]]) == 10


def test_maximumWealth_3():
    assert maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]) == 17


def test_maximumWealth_4():
    assert maximumWealth([[1, 2, 3], [3, 2, 1], [5, 6, 7]]) == 18


def test_maximumWealth_5():
    assert maximumWealth([[4, 6, 8], [5, 7, 9]]) == 21
