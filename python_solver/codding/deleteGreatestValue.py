def deleteGreatestValue(grid: list[list[int]]) -> int:
    column = len(grid[len(grid)-1])
    sums = 0
    for g in grid:
        g.sort()
        g.reverse()

    for i in range(column):
        sums+= max(g[i] for g in grid)   
         
    return sums