from codding.twoSumProblem import twoSum


def test_twoSum_1():
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]


def test_twoSum_2():
    assert twoSum([3, 2, 4], 6) == [1, 2]


def test_twoSum_3():
    assert twoSum([3, 3], 6) == [0, 1]


def test_twoSum_4():
    assert twoSum([1, 3, 5, 7], 6) == [0, 2]


def test_twoSum_5():
    assert twoSum([11, 13, 15, 17, 19, 21, 23], 40) == [4, 5]
