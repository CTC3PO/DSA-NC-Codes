#INITIALIZE TREE NODE: 
class TreeNode: 
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

#INSERT a new node and return the root of the BST
def insert (root,val):
    if not root:
        return TreeNode(val)
    if val > root.val: 
        root.right = insert(root.right, val) 
    elif val < root.val: 
        root.left = insert(root.left, val)
    return root 

# REMOVE a node and return the root of the BST
def remove(root, val):
    if not root: 
        return None     
    if val > root.val: 
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else: 
        #simple case: node has 0 or 1 child: 
        if not root.left: 
            return root.right
        elif not root.right: 
            return root.left
        #else: recursively look and remove the node 
        else: 
            minNode = minValueNode(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val) 
    return root 

# Helper function - Return the min value node of the BST
def minValueNode(root):
    curr = root 
    while curr and curr.left:
        curr = curr.left
    return curr

# Note: when removing a root node, better to replace it with a leaf note
# using either the largest left-leaf node, or the smallest right-leaf node
    