# Heap or Priority Queue: 
# 1. structure property: it's a balanced binary tree, meaning every
# level is filled with nodes, except the last level. 
# 2. recursive order property: the order is preserved from root node to its sub-tree
# if it's a min heap, that means its sub trees (both left and right) are > root node
# this order applies to all its sub-trees and sub-sub trees until the last level. 
# if it's a MAX heap, the root node > all its sub-trees and sub-sub trees, etc.  


# Example below illustrates a MIN HEAP
# code for PUSH and POP

class Heap: 
    # initialize a heap, the first index (0) contains a dummy value
    def __inint__(self):
        self.heap = [0]
    
    # PUSH : add value to last (end of array), then percolate up
    # compare value at i to its parent, if < its parent, swap
    # keep comparing child node with its parent until reaching 
    # desired location where parent node < child node (for min heap) 
    #TIME COMPLEXITY: O(logn)
    
    def push(self, val): 
        # first, append the value to end of heap (end of array)
        # then get the ith index of the just added value
        self.heap.append(val)
        i = len(self.heap) - 1

        # Percolate up - compare it with its parent, swap 
        # until reaching the location where parent node < child node
        while self.heap[i] < self.heap[i//2]:
            temp = self.heap[i]
            self.heap[i] = self.heap[i//2]
            self.heap[i//2] == temp
            i = i // 2
    
    # POP: 
    # when pop, have to maintain structure and recursive order property
    # PERCOLATE DOWN: take the last value and put it to the root node, then
    # percolate down, keep comparing it ot its children, if > than children,
    # swap it, until reaching desired location where it meets recursive order property
    
    #TIME COMPLEXITY: O(logn) - ( which is the height of the tree, n is no. of elements in array)
def pop (self): 
    # check if len of heap = 1, it means it only contains dummy value, return none
    if len(self.heap) == 1: 
        return None
    # check if len of heap == 2, meaning it only has 1 value, pop out to return that value
    if len(self.heap) == 2: 
        return self.heap.pop() 
    
    # result (variable) is the one to be returned in the end, result is the root value to be pop out
    result = self.heap[1]
    # then, replace root node with the last node of the heap (move it up)
    self.heap[1] = self.heap.pop()

    # start at i = 1, look to PERCOLATE down the new root node, keep swapping it 
    # with its left or right child until it's at a desired location (meaning
    # maintaining the order structure)
    i = 1 

    # while there's nodes in the level (for a balanced tree, there's always left node if there's right node), 
    # meaning, the index at left node is < length of the heap ( for example: in 2 level bt,
    # index at left child node is 2, while length of the heap is 3)

    while 2 * i < len(self.heap):
        # check for child node to swap, in the first case, where's there's also a right node 
        # and left child > right child and node at i > right child: 
        if 2 * i + 1 < len(self.heap) and self.heap[ 2 * i] > self.heap [2 * i +1] and self.heap[i] > self.heap [2 * i +1]:
            #swap the node with its right child node: 
            temp = self.heap[i]
            self.heap[i] = self.heap[ 2 * i +1]
            self.heap[2 * i + 1] = temp
            # move index to the right child node to keep percolating down (if needed) 
            i = 2 * i + 1
        
        # otherwise, if there's only left node, and node at i > left child node (node at 2 * i):
        elif self.heap[i] > self.heap[2 * i]:
            # swap node at i with its left child node: 
            temp = self.heap[i]
            self.heap[i] = self.heap[2 * i]
            self.heap[2 * i] = temp
            # then, move on to the next index of the current left child node to keep percolating: 
            i = i * 2

        # if condition is met, meaning tree has retained its order property
        # (parent node < its child nodes), break out of the loop
        else: 
            break 
    
    # return the result value (which is the first node that was popped out from the tree)
    return result 