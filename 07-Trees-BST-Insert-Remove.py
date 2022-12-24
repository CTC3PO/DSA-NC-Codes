#INITIALIZE TREE NODE: 
class TreeNode: 
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

#BST: base case: has 0/1 child
#INSERT a new node and return the root of the BST
def insert (root,val):
    # if tree is empty (not root), add the new TreeNode to the tree
    if not root:
        return TreeNode(val)
    # otherwise, compare the val to root.val, pass it to the left
    # of the tree if val < root.val, pass to the right of the 
    # tree if val > root.val, then recursively do that until 
    # inserting in the right position 
    if val > root.val: 
        root.right = insert(root.right, val) 
    elif val < root.val: 
        root.left = insert(root.left, val)
    return root 

# REMOVE a node and return the root of the BST
# When remove, 2 cases: 1.node has 0 or 1 child
# 2. node has 2 children. 
def remove(root, val):
    # if the tree is empty (no root node), return nothing
    if not root: 
        return None     

    # check if the val is > or < than root.val
    if val > root.val: 
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)

    #otherwise, check if the node has only 1 node (either
    # left or right, if yes, remove its child)
    else: 
        #simple case: node has 0 or 1 child: 
        if not root.left: 
            return root.right
        elif not root.right: 
            return root.left
        
        # else: the node has 2 children, 
        # recursively look and remove the node, replace
        # the node with the min node of the right sub-tree 
        else: 
            minNode = minValueNode(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val) 
    return root 

# Helper function - to get the min value node of the right sub-tree 
def minValueNode(root):
    curr = root 
    while curr and curr.left:
        curr = curr.left
    return curr

# Note: when removing a root node, better to replace it with a leaf node
# using either the largest left-leaf node, or the smallest right-leaf node
    