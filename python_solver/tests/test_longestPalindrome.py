from codding.longestPalindrome import longestPalindrome


def test_longestPalindrome_1():
    assert longestPalindrome("babad") == "bab"


def test_longestPalindrome_2():
    assert longestPalindrome("cbbd") == "bb"


def test_longestPalindrome_3():
    assert longestPalindrome("abccddccb") == "bccddccb"


def test_longestPalindrome_4():
    assert longestPalindrome("abcde") == "a"


def test_longestPalindrome_5():
    assert longestPalindrome("a") == "a"
