from codding.intToRoman import intToRoman

def test_intToRoman_1():
    assert intToRoman(10000) == ""

def test_intToRoman_2():
    assert intToRoman(-1) == ""

def test_intToRoman_3():
    assert intToRoman(1994) == "MCMXCIV"

def test_intToRoman_4():
    assert intToRoman(9999) == "ĪẌCMXCIX"

def test_intToRoman_5():
    assert intToRoman(0) == ""