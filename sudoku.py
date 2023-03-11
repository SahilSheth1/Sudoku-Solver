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

print("Given Puzzle: \n")
print("'0' is equivalent to blank spots \n")
print(np.matrix(grid))
print("\n")

def possibleSolution(row, column, number):
    global grid
    
    for x in range(0, 9):
        if grid[row][x] == number:
            return False
        
    for y in range(0, 9):
        if grid[y][column] == number:
            return False
        
    x0 = (row // 3) * 3
    y0 = (column // 3) * 3
    
    for x in range(0, 3):
        for y in range(0, 3):
            if grid[x0 + x][y0 + y] == number:
                return False
            
    return True

def solvePuzzle():
    global grid
    
    for row in range(0, 9):
        for column in range(0, 9):
            if grid[row][column] == 0:
                for number in range(1, 10):
                    if possibleSolution(row, column, number):
                        grid[row][column] = number
                        solvePuzzle()
                        grid[row][column] = 0
                
                return
    print("Solution to Puzzle: \n")
    print(np.matrix(grid))
    
solvePuzzle()