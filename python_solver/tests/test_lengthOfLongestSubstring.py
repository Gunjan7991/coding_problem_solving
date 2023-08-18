from codding.lengthOfLongestSubstring import lengthOfLongestSubstring

def test_lengthOfLongestSubstring_1():
    assert lengthOfLongestSubstring("abcabcbb")==3

def test_lengthOfLongestSubstring_2():
    assert lengthOfLongestSubstring("bbbbb")==1

def test_lengthOfLongestSubstring_3():
    assert lengthOfLongestSubstring("pwwkew")==3

def test_lengthOfLongestSubstring_4():
    assert lengthOfLongestSubstring("ohhhhhhujurterateraterasukuuuuasdfghjkl")==10

def test_lengthOfLongestSubstring_5():
    assert lengthOfLongestSubstring("aabcdecfghijkll")==10