from codding.romanToInt import romanToInt

def test_romanToInt_1():
    assert romanToInt("III") == 3

def test_romanToInt_2():
    assert romanToInt("LVIII") == 58
  
def test_romanToInt_3():
    assert romanToInt("MCMXCIV") == 1994
  
def test_romanToInt_4():
    assert romanToInt("MC") == 1100
  
def test_romanToInt_5():
    assert romanToInt("O") == 0
  