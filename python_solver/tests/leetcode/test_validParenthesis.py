from leetcode.validParenthesis import isValid


def test_isValid_1():
    assert isValid("()") == True


def test_isValid_2():
    assert isValid("()[]{}") == True


def test_isValid_3():
    assert isValid("(]") == False


def test_isValid_4():
    assert isValid("[") == False


def test_isValid_5():
    assert isValid("]") == False
