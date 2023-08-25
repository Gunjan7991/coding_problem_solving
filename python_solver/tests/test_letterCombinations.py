from codding.letterCombination import letterCombinations

def test_letterCombinations_1():
    assert letterCombinations("23")  == ["ad","ae","af","bd","be","bf","cd","ce","cf"]

def test_letterCombinations_2():
    assert letterCombinations("2")  == ["a","b","c"]

def test_letterCombinations_3():
    assert letterCombinations("")  == []

def test_letterCombinations_4():
    assert letterCombinations("234")  == ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]

def test_letterCombinations_5():
    assert letterCombinations("21")  == []
