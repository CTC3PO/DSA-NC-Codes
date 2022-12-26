''' Adjacency list, we can use either GraphNode to represent,
or can use HahsMap (simpler) '''

# Example using GraphNode: 
class GraphNode: 
    def __init__(self,val):
        self.val = val
        self.neighbors = []

# Example using HashMap
adjList = {"A" : [], "B" : []}

# Given directed edges, we can build an adjacency list
edges = [ ["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"] ]

# Initialize adjacency list as empty hashmap
adjList = {}

# then, for source and destination node, if not exist in 
# adjacency list, add them, if already aexist, append the 
# destination to source node
for src, dst in edges: 
    if src not in adjList: 
        adjList[src] = []
    if dst not in adjList: 
        adjList[dst] = []
    # otherwise, add it to adjList
    adjList[src].append(dst)

# DFS on Adjacency List (Backtracking) 
# Count no of paths can go from node to target
# TIME COMPLEXITY: N ^ V (V: height, N: average no of edges) 
def dfs( node, target, adjList, visit): 
    # check if node already visited (here don't need to check for out of bounds)
    if node in visit: 
        return 0 
    if node == target: 
        return 1
    
    # Start count at 0
    count = 0

    visit.add(node) 

    for neighbor in adjList[node]: 
        count += dfs(neighbor, target, adjList, visit) 
    
    visit.remove(node) 

    return count


# BFS (length of shortest path) 
# What's the shortest path (length) to go from node to target

# TIME COMPLEXITY: O ( V + E) 
# SPACE COMPLEXITY: O (V) (there's a max V vertices it has to traverse) 

from collections import deque

def bfs (node, target, adjList): 
    length = 0
    visit = set()
    queue = deque() 
    queue.append(node) 
    visit.add(node) 

    # start w length = 0 
    length = 0
    
    # on the queue (level), go to each node in the queue, 
    
    while queue: 
        for node in len(queue): 
            current = queue.popleft() 
            # if the node is target, return length (level) of that
            # queue.
            if current == target: 
                return length
            
            # If not, add the node's neighbors to the queue 
            # and visit hshmap. 
            for neighbor in adjList[current]: 
                if neighbor not in visit: 
                    queue.append(neighbor) 
                    visit.add(neighbor) 
        
        # increase the length and go to next level, and go
        # the nodes of that level again
        length += 1
    
    return length




