from codding.deleteGreatestValue import deleteGreatestValue

def test_deleteGreatestValue_1():
    assert deleteGreatestValue([[1,2,4],[3,3,1]]) == 8

def test_deleteGreatestValue_2():
    assert deleteGreatestValue([[]]) == 0

def test_deleteGreatestValue_3():
    assert deleteGreatestValue([[1,2,4]]) == 7

def test_deleteGreatestValue_4():
    assert deleteGreatestValue([[1,2,4],[3,3,1],[5,5,5]]) == 15

def test_deleteGreatestValue_5():
    assert deleteGreatestValue([[1,2,4],[3,3,1], [4,2,2]]) == 9
