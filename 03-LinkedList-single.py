# Initialize ListNode
class ListNode: 
    def __init__(self, val):
        self.val = val
        self.next = None

# Implementation of Singly Linked list
class LinkedList: 
    def __init__(self):
        # Init the list with a "dummy" node which makes
        # removing a node from the beginning of the list easier
        self.head = ListNode(-1)
        self.tail = self.head
    
    # INSERT END 
    def insertEnd(self, val):
        # point the current tail to the new listnode 
        # then set the new node's tail as tail 
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    # REMOVE AT INDEX
    def remove(self,index): 
        # start w. i at 0 and current points to head node 
        i = 0
        current = self.head
        # keep moving up current pointer until before the target index: 
        while i < index and current: 
            i += 1
            current = current.next
        
        # Remove the node ahead of current
        if current: 
            current.next = current.next.next

    # PRINT
    def print(self):
        current = self.head.next 
        while current: 
            print(current.val, " -> ")
            current = current.next 
        print() 