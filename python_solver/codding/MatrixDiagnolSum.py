def diagonalSum(mat: list[list[int]]) -> int:
    total = 0
    i = 0 
    j =len(mat)-1
    for k in range(len (mat)):
        pos0 = mat[i][k] 
        pos1 = mat[k][j]
        if (len(mat)-1)%2==0  and  i==j:
            total += pos0
        else:
            total += pos0+pos1

        i+=1
        j-=1
        
    return total


if __name__ == "__main__":
    if diagonalSum([[1,2,3],[4,5,6],[7,8,9]]) == 25:
        print("Passed")
    else:
        print("Failed")
    if diagonalSum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]) == 8:
        print("Passed")
    else:
        print("Failed")
    if diagonalSum([[5],]) == 5:
        print("Passed")
    else:
        print("Failed")