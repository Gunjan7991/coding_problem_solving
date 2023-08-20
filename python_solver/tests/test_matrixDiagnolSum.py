from codding.MatrixDiagnolSum import diagonalSum

def test_diagonalSum_1():
    assert diagonalSum([[1,2,3],[4,5,6],[7,8,9]]) == 25

def test_diagonalSum_2():
    assert diagonalSum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]) == 8

def test_diagonalSum_3():
    assert diagonalSum([[5],]) == 5

def test_diagonalSum_4():
    assert diagonalSum([[0],]) == 0

def test_diagonalSum_5():
    assert diagonalSum([[1,2],[3,4]]) == 10
