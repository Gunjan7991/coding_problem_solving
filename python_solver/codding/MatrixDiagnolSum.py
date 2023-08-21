def diagonalSum(mat: list[list[int]]) -> int:
    total = 0
    i = 0
    j = len(mat) - 1
    for k in range(len(mat)):
        pos0 = mat[i][k]
        pos1 = mat[k][j]
        if (len(mat) - 1) % 2 == 0 and i == j:
            total += pos0
        else:
            total += pos0 + pos1

        i += 1
        j -= 1

    return total
