'''  Count no. of unique paths from Top left to bottom right. 
Only move Down or Right one by one

With 2D dynamic programming, if moving from the bottom up, 
it will results in the pattern below, every current grid [r]c]
index = its right + its below value

    | 20  | 10 | 4  | 1  |
    ----------------------
    | 10  |  6 |  3 | 1  |
    ----------------------
    |  4  |  3 |  2 | 1  |
    ----------------------
    |  1  |  1 | 1  | 1  |  (for Bottom up DP, this is the first prevRow), then keep 
                            moving up 1 row and loop through the cols position in each row
    
'''

#--------------------------------------------------------------------------------
# BRUTE FORCE SOLUTION (RECURSION) 
def bruteforce (r, c, rows, cols):
    # check if the r or c index is out of bounds (= 4 or length of rows/cols) 
    if r == rows and c == cols: 
        return 0
    
    # check if it reaches the last posiiton in the grid [rows-1][cols-1]
    if r == rows -1 and c == cols -1:
        return 1
    
    #otherwise, apply the recursion problem on the next row and column position
    return ( bruteforce (r + 1, c, rows, cols) 
            + bruteforce(r, c + 1, rows, cols) )

#--------------------------------------------------------------------------------
# MEMOIZATION APPROACH ( TOP-DOWN DYNAMIC PROGRAMMING)
# TIME and SPACE COMPLEXTIY: O(m*n) 

def memoization (r, c, rows, cols, cache): 
    # check if the r or c index is out of bounds (= 4 or length of rows/cols) 
    if r == rows or c == cols: 
        return 0

    # check if it reaches the last posiiton in the grid [rows-1][cols-1]
    if r == rows -1 and c == cols - 1: 
        return 1
    
    # otherwise, keep going, and cache the repeated position value
    if cache[r][c] > 0: 
        return cache[r][c]
    
    cache[r][c] = ( memoization( r + 1, c, rows, cols, cache) 
                    + memoization(r, c + 1, rows, cols, cache) 
                    )                    
    return cache[r][c]

#--------------------------------------------------------------------------------
# BOTTOM-UP DYNAMIC PROGRAMMING SOLUTION 
def dp (rows, cols): 

    # start from the bottom of the grid - fill the out of bound
    # index row (row index = 4) with 0's
    prevRow = [0] * cols

    # then, loop through all the rows, starting from the last row(index = 3) 
    # rows -1 is the last row, up to row index 0, every step move up 1 index: 
    for r in range (rows - 1, -1, -1):
        # First, fill the current row with all 0's
        currRow = [0] * cols
        # then fill the current row, last column index with 1
        currRow[cols - 1] = 1

        # for each row, moving up 1 by 1 in the columns, starting with second to last col
        for c in range (cols - 2, -1, -1):
            currRow[c] = currRow[c + 1] + prevRow[c]

        # after looping through all the positions in the columns of each row, 
        # set the prevRow as the current row to keep moving up to the next row:
        prevRow = currRow
    
    # at last, we reach index [r][c] = [0][0], return it
    return prevRow[0] 
