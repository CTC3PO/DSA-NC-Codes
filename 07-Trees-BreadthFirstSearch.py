from collections import deque

#INITIALIZE a TreeNode: 
class TreeNode: 
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Function for Breadth-first-search (BFS)
# how to add nodes to process? use QUEUE Ds
# add elements to the queue (FIFO) - whatever
# added first will be processed first
def dfs(root): 
    queue = deque()

#add root node to the que
    if root: 
        queue.append(root)

    # keep track of the level we're on in the tree, start at 0 for root lv
    level = 0

# append nodes to the que while there's still nodes to add (level not empty)
    while len(queue) > 0:
        print("level: ", level)
        # print every nodes in that level 
        # len of que is the number of items on that level         
        for i in range(len(queue)):
            # pop out and print that value
            current = queue.popleft()
            print(current.val)
            #add any current's left and right child to the queue
            # add from left to right
            if current.left: 
                queue.append(current.left)
            if current.right: 
                queue.append(current.right) 
        #increase the lv by 1 to go to the next lv's nodes
        level +=1   

# TIME COMPLEXITY: O(n)  
# don't be fool by the nested while & for loop
# (we only traveser each node once)
        