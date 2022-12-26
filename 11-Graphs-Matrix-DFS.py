''' QUESTION: count the unique paths from the top left to the bottom right.
A single path can only moves along O's and can't visit hte same cell more than one.

example graph: (0: free vertice, 1: blocked vertice) 

    0   0   0   0   
    1   1   0   0
    0   0   0   1
    0   1   0   0

'''

def dfs (grid, r, c, visit):    # r, c is the index of row and column 
    # Get len of row and cols: 
    ROWS, COLS = len(grid), len(grid[0])

    # edge cases for where the vertices can move: 1. out of bounds
    # (<0 index or > last index), or visited a blocked vertice (1)
    # or visit already visited path (visit is the hash set)
    if ( min(r,c) < 0   
    or r == ROWS or c == COLS 
    or (r,c) in visit 
    or grid[r,c] == 1 ):    # blocked vertice
        return 0

    # return 1 if found a path: meaning 
    # reaching the last index for row and column
    if r == ROWS - 1 and c == COLS - 1: 
        return 1

    # add the vertice to the already visited (hash set)
    visit.add ((r,c))

    # Start the count of paths = 0 
    count = 0

    # then recursively try to traverse the vertice to its up, down, left,
    # and right position, look for the next vertice it can pass to, 
    # order of traversing: down, up, right, left (r+1, r-1, c+1, c-1)
    count += dfs (grid, r + 1, c, visit)
    count += dfs (grid, r - 1, c, visit)
    count += dfs (grid, r, c + 1, visit) 
    count += dfs (grid, r, c - 1, visit) 

    # remove the vertice from the path, to backtracking up to find    
    # another legible path, adding 1 to the count if successfuly 
    # found another path. Keep backtracking until reaching the first vertice.
    # The new path can visit the same position as previous valid path,
    # to allow to find another path, but a single path can only visit a
    # position once 
    visit.remove((r,c))

    # return the total count (of paths) 
    return count 

    # NOTE: 
    # TIME COMPLEXITY: O (4 ^ (m*n)) , m, n is the len of rows and columns
    # SPACE COMPLEXITY: O(m*n) 
