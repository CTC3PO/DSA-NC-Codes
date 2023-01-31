class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

# IMPLEMENTATION For Doubly linked list
class LinkedList:
    def __init__(self):
        #Initialize the list with "dummy" head and tail nodes
        # which makes edge cases for insert and remove easier. 
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.next = self.head

    # INSERT IN FRONT
    def insertFront(self,val):
        newNode = ListNode(val)
        newNode.prev = self.head
        newNode.next = self.head.next 

        self.head.next.prev = newNode
        self.head.next = newNode

    # INSERT AT END
    def insertEnd(self, val): 
        newNode = ListNode(val)
        newNode.next = self.tail
        newNode.prev = self.tail.prev

        self.tail.prev.next = newNode
        self.tail.prev = newNode

    # REMOVE FRONT
    def removeFront(self):
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next

    # REMOVE END
    def removeEnd(self):
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev  

    #PRINT 
    def print(self):
        curr = self.head.next
        while curr != self.tail: 
            print(curr.val, " -> ")
            curr = curr.next
        print() 
