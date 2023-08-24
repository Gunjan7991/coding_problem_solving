from codding.longestCommonPrefix import longestCommonPrefix

def test_longestCommonPrefix_1():
    assert longestCommonPrefix(["flower","flow","flight"]) == "fl"

def test_longestCommonPrefix_2():
    assert longestCommonPrefix(["dog","racecar","car"]) == ""

def test_longestCommonPrefix_3():
    assert longestCommonPrefix(["aaa","aaa","aa"]) == "aa"

def test_longestCommonPrefix_4():
    assert longestCommonPrefix([""]) == ""

def test_longestCommonPrefix_5():
    assert longestCommonPrefix(["a"]) == "a"

