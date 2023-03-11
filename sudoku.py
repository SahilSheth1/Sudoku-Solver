import numpy as np

grid = [[0, 6, 8, 0, 0, 0, 9, 3, 0],
        [0, 4, 2, 0, 0, 0, 6, 0, 0],
        [1, 9, 0, 0, 8, 0, 0, 4, 0],
        [0, 8, 5, 2, 0, 1, 0, 0, 7],
        [7, 0, 0, 8, 9, 0, 0, 0, 0],
        [2, 0, 9, 0, 0, 7, 5, 0, 3],
        [0, 2, 0, 1, 0, 0, 0, 5, 0],
        [8, 5, 0, 0, 4, 0, 7, 6, 0],
        [4, 7, 3, 0, 5, 2, 0, 0, 9]]

print(np.matrix(grid))

def possibleSolution(row, column, number):
    global grid
    
    for x in range(0, 9):
        if grid[row][x] == number:
            return False
        
    for y in range(0, 9):
        if grid[y][column] == number:
            return False