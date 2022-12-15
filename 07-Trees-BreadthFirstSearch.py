from collections import deque

#INITIALIZE a TreeNode: 
class TreeNode: 
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Function for Breadth-first-search (BFS)
def dfs(root): 
    que = deque()

#add root node to the que
    if root: 
        que.append(root)

    # keep track of the level we're on in the tree, start at 0 for root lv
    level = 0

# append nodes to the que while there's still nodes to add (not null)
    while len(que) > 0:
        print("level: ", level)
        #len of que is the number of items on that level 
        for i in range(len(que)):
            current = que.popleft()
            print(current.val)
            #add any current's left and right child to the que
            if current.left: 
                que.append(current.left)
            if current.right: 
                que.append(current.right) 
        #increase the lv by 1 to go to the next lv's nodes
        level +=1   

# TIME COMPLEXITY: O(n)  
# don't be fool by the nested while & for loop
# (we only traveser each node once)