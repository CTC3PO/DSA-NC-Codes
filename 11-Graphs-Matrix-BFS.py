''' QUESTION: find the shortest path from the top left to bottom right.

example graph: (0: free vertice, 1: blocked vertice) 

    0   0   0   0   
    1   1   0   0
    0   0   0   1
    0   1   0   0

With Breath-first-search, we visit each layer, go to all its vertices, for the 
first vertice it go to, also add the neighbors of that vertice to the visit
hash set - this will ensure when we get to the other vertice in the same level, 
if their neighbors are the same, those neighbors won't be added as other vertice
's neighbors. This technique results in a better time complexity > DFS. 

'''

from collections import deque

grid = [[0,0,0,0], 
        [1,1,0,0], 
        [0,0,0,1], 
        [0,1,0,0]]      
                
# Shortest path from top left to bottom right: 
def bfs(grid): 
    # get the number of rows and cols in grid: 
    ROWS, COLS = len(grid), len(grid[0])

    # create a queue to keep track of the level we're on, 
    # visit hashset to keep track of already visited vertices 
    # add the first node to both queue and visit hashset 
    queue =  deque() 
    visit = set() 
    queue.add ((0,0))
    visit.add((0,0))

    # start at length = 0 for the path
    length = 0 

    # while on that level, visit each vertice in that queue
    while queue: 
        for i in range (len(queue)):
            # pop out the current vertice 
            r,c = queue.popleft() 

            # check if already reach destination (last index for r and c) 
            if (r == ROWS - 1 and c == COLS -1):
                return length

            # otherwise, look to the vertice's neighbors positions (R, L, U, D): 
            neighbors = [ [0,1], [0,-1], [1,0], [-1,0] ]
            
            # keep going (continue) if the vertice should not be part 
            # of the path (out of bounds, already visited, or in blocked position)
            # dr and dc is the different in r and c (+1 , -1, like in the neighbors)
            for dr, dc in neighbors:    
                if ( min(r + dr, c + dc) < 0 
                or r + dr == ROWS or c + dc == COLS
                or (r + dr, c + dc) in visit
                or grid[r + dr][c + dc] == 1]
                ):
                continue 

            # Otherwise, add the current vertice's neighbors to the queue and visit set
            # add these to hashset will ensure that the other vertice in the 
            # same level won't traverse those neighbor nodes again 
            queue.append((r + dr, c + dc))
            visit.append((r + dr, c + dc))

            # increase the length by 1 after done visiting that level (queue)
        length += 1

# NOTE: 
# TIME COMPLEXITY: O (m*n) - m and n is the len of rows and cols 
# SPACE COMPLEXITY: O (m*n) - m * n is the max size