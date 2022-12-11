# Question: determine if a path exists from the root of a tree 
# to a leaf node, it may not contains any zero 

#initialize TreeNode: 
class TreeNode: 
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Function that return True if there exists a path: 
def canReachLeaf(root):
    #return False if root is null or = 0
    if not root or root.val == 0:   
        return False
    
    #return True if reached leaf node (meaning, it has no left and right node)
    if not root.left and not root.right:    #
        return True

    #otherwise, if not yet reached leaf node, check left and 
    # right sub-tree (recursively) and see if it contains a path
    if canReachLeaf(root.left):    
        return True
    if canReachLeaf(root.right):
        return True

    #lastly, if can't find path, return False 
    return False 

# Function that return the path found through backtracking technique: 
# the path is a dynamic array that appends nodes that satisfy condition above
def leafPath(root, path):
    #return False if root is null or = 0, append root's val
    if not root or root.val == 0:
        return False
    path.append(root.val) 

    #return True if reached leaf node (meaning, it has no left and right node)
    if not root.left and not root.right:
        return True

    #otherwise, if not yet reached leaf node, check left and 
    # right sub-tree (recursively) and see if it contains a path
    if leafPath(root.left, path):
        return True
    if leafPath(root.right, path):
        return True
    #pop the value out of the path if not satisfy no 0-path
    path.pop()

    return False 


