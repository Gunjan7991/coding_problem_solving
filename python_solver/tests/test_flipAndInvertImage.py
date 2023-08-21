from codding.flipAndInvertImage import flipAndInvertImage


def test_flipAndInvertImage_1():
    assert flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]) == [
        [1, 0, 0],
        [0, 1, 0],
        [1, 1, 1],
    ]


def test_flipAndInvertImage_2():
    assert flipAndInvertImage(
        [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    ) == [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]


def test_flipAndInvertImage_3():
    assert flipAndInvertImage([[1, 1], [0, 0]]) == [[0, 0], [1, 1]]


def test_flipAndInvertImage_4():
    assert flipAndInvertImage([[1, 0], [0, 1]]) == [[1, 0], [0, 1]]


def test_flipAndInvertImage_5():
    assert flipAndInvertImage([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == [
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
    ]
