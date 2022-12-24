# BST is sorted tree, left sub-tree < root, right sub-tree > root
# to search: go to the right of the tree if target > root value
# go to the left of the tree if target < root value
# recursively look for target and traverse the tree until finding
# the target 

# Balanced tree (if the height of the left and right is roughly equal)
# mearning the difference in their level should be <= 1

# COMPLEXITY: O (h) - the heihgt of the tree
# but for simplicity: we use O(logn)

# WHY BST OVER SORTED ARRAY (using binary search?) 
# --> Insert and Delete is more efficient than array 
# Array: O(n) vs. BST (insert/delete): O(logn)

#initialize a TreeNode: 
class TreeNode: 
    def __init__(self, val):
        self.val - val
        self.left = None
        self.right = None

# Function search in BST: 

def search(root, target):
    #base case, no root node, return False
    if not root: 
        return False
    # otherwise, recursively search on the right or left depending
    # on if the target is > or < root node. if target = root, return true
    if target > root.val: 
        return search(root.right, target)
    elif target < root.val: 
        return search(root.left, target)
    else: 
        return True


