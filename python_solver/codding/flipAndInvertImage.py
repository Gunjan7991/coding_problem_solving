def flipAndInvertImage(image: list[list[int]]) -> list[list[int]]:
    flipped = []
    for i in range(0, len(image)):
        temp = []
        for j in range(len(image[i]) - 1, -1, -1):
            if image[i][j] == 1:
                temp.append(0)
            else:
                temp.append(1)
        flipped.append(temp)
    print(flipped)
    return flipped
