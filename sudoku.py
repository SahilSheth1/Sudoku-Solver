# Import Numpy library

import numpy as np

# Create Grid with numbers from unsolved puzzle
# Also the input as of right now

grid = [[2, 0, 0,   0, 4, 0,    0, 5, 7],
        [0, 0, 1,   0, 0, 8,    0, 0, 0],
        [4, 0, 6,   0, 0, 0,    1, 3, 0],
        
        [0, 3, 5,   0, 0, 6,    0, 0, 0],
        [0, 7, 9,   4, 8, 5,    2, 1, 0],
        [0, 2, 4,   1, 3, 0,    6, 9, 5],
        
        [0, 0, 2,   7, 1, 0,    0, 0, 0],
        [0, 0, 0,   8, 0, 2,    0, 6, 1],
        [5, 0, 0,   0, 0, 0,    7, 0, 0]]

# Function to check if tile or slot can have the given number as a solution
# If given number cannot be solution, function returns false

def possibleSolution(row, column, number):
    global grid
    
    # Check the columns to see if tile or slot can be a solution
    
    for x in range(0, 9):
        if grid[row][x] == number:
            return False

    # Check the rows to see if tile or slot can be a solution
    
    for y in range(0, 9):
        if grid[y][column] == number:
            return False
    
    # Check the box to see if tile or slot can be a solution
    
    x0 = (row // 3) * 3
    y0 = (column // 3) * 3
    
    for i in range(0,3):
        for j in range(0,3):
            if grid[x0 + i][y0 + j] == number:
                return False

    return True

# Function to solve the actual puzzle

def solve():
    global grid
    
    # Loops to iterate through every tile and row with every number
    
    for row in range(0, 9):
        for column in range(0, 9):
            if grid[row][column] == 0:
                for number in range(1, 10):
                    
                    # Check if tile/slot has a possible solution with number
                    
                    if possibleSolution(row, column, number):
                        grid[row][column] = number
                        solve() # Recursion
                        grid[row][column] = 0

                return
    
    # Print final solved Sudoku Puzzle
      
    print(np.matrix(grid))
    print("\n")

solve()