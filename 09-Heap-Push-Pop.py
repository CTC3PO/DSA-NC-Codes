# MIN HEAP code for PUSH and POP

class Heap: 
    #initialize heap
    def __init__(self):
        self.heap = [0]

    # PUSH
    def push(self, val):
        # first, add the value to the end of the heap and get the last index 
        self.heap.append(val)
        i = len(self.heap) - 1
    
        # Percolate up: 
        # while the child node value < parent's value, swap child and parent 
        while i > 1 and self.heap[i] < self.heap[ i //2]:
            temp = self.heap[i]
            self.heap[i] = self.heap[i//2]
            self.heap[i//2] = temp
            # go up 1 level to the parent node
            i = i // 2
    
    # POP: 
    def pop(self): 
        # if heap's len is 1, which means it only 
        # contains a dummy variable, return none
        if len(self.heap) == 1: 
            return None
        # if heap's len is 2, meaning it only contains 1 node,
        #  return that only node
        if len (self.heap) == 2: 
            return self.heap.pop() 
        
        #otherwise, start with root node and move the last node's value to root: 
        result = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1

        # Then, percolate down:
        # while there's a left-child node (meaning, len of heap > left child index) 
        while 2 * i < len(self.heap): 
            # if it satisfies all these 3 conditions, then swap right child
            # 3 conditions: there's a right child node + right child node < left child node
            # and value at current node > right child node
            if (2 * i + 1 < len(self.heap) and 
            self.heap[2 * i +1] < self.heap[2*i] and
            self.heap[i] > self.heap [2*i+1]):
                # SWAP RIGHT CHILD: 
                temp = self.heap[i]
                self.heap[i] = self.heap [2*i+1]
                self.heap[2*i+1] = temp 
                # then move down to next right child node 
                i = 2 * i + 1
            
            #otherwise, see if current node > left child node, then swap
            elif self.heap[i] > self.heap[2*i]:
                # SWAP LEFT CHILD: 
                temp = self.heap[i]
                self.heap[i] = self.heap [2 * i]
                self.heap [2*i] = temp
                # then move down to next left child node 
                i = 2 * i 
            else: 
                break
        return result