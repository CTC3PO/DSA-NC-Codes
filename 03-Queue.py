class ListNode: 
    def __init__(self,val):
        self.val = val
        self.next = None

# QUEUE - FIFO (first in, first out)   
class Queue: 
    # Implementing this with dummy nodes would be easier:
    def __init__(self):
        self.left = self.right = None
    
    # ENQUEUE (push - to the right ) 
    def enqueue(self, val):
        newNode = ListNode(val) 

        # if Queue is non-empty (has a right node)
        if self.right: 
            self.right.next = newNode
            # set the new node as the current right node (it will be added to the right)
            self.right = self.right.next 
        # otherwise, if queue is empty, add the first node to queue
        else: 
            self.left = self.right = newNode 

    # DEQUEUE (pop) 
    def dequeue(self): 
        # when queue is empty, nothing ot remove:  
        if not self.left: 
            return None
        
        # remove left node and return value: 
        val = self.left.val 
        # remove by simple point the currnet left node to the one after it
        self.left = self.left.next 
        return val 

    # PRINT
    def print(self):
        current = self.left
        while current: 
            print (current.val, " -> ", end = "")
            current = current.next 
        print()  # new line 
        