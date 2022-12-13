# DFS: go as deep to the sub-tree (left or right) until hitting leaf node
# before go deep into the other sub-tree
# (recursively run DFS in each sub-tree)

#INITIALIZE a TreeNode: 
class TreeNode: 
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# 3 way to Traverse: INORDER, PREORDER, POSTORDER 
# INORDER traversal
def inorder(root):
    if not root: 
        return
    inorder(root.left)
    print(root.val)   # print after traverse 1 sub-tree (left)
    inorder(root.right)

# PRE-ORDER traversal
def preorder(root):
    if not root: 
        return
    print(root.val)     # print before traverse any sub-tree
    inorder(root.left)    
    inorder(root.right)

# POST-ORDER traversal
def postorder(root):
    if not root: 
        return
    inorder(root.left)    
    inorder(root.right) 
    print(root.val)     # print after traverse all the sub-trees