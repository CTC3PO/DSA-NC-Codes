import heapq

# HEAPIFY: build heap, when given a list of values, we can take those 
# values and turn them into a heap in O(n) time. 
# start with last node, then compare with its parent node
# we can skip half the array, taking i // 2, we'll start with
# the node at i // 2 location, then move up 1 value at a time, 
# then percolate down by comparing that value with its children (
# left and right child, until order property is maintained)

# TIME COMPLEXITY: O(n) for heapify, 
# to pop tree: O(logn) for each value, and there's n value
# so it takes O(n logn) to pop the whole tree ==> we
# can sort value in O(n logn) time 
''' SEARCH (max/min)      SEARCH(mid)     INSERT/POP
        O(1)                O(logn)         O(logn)'''

# example - heapify for a MIN HEAP
class Heap: 

    # function: Heapify:
    def heapify(self, arr): 
        # 0-th position is moved to the end
        arr.append(arr[0])

        # initialize heap as the array
        self.heap = arr

        # we'll start with the current position at half the position of the last element
        current = (len(self.heap) - 1) // 2

        # going into the while loop until current hits 0, we move from the current node and
        # move up 1 position at a time, each time compares that value wiht its left and right node        
        while current > 0: 
            # start with i as current index 
            i = current

            # at the current index, if there's at least left child, and right child < left child
            # and right child < node at current, swap current and right child
            while 2 * i < len(self.heap):
                if (2 * i < len(self.heap) and self.heap[2 * i + 1] < self.heap[2 * i] and self.heap[ 2 * i + 1] < self.heap[i]): 
                    # swap node at i (curent node) and its right child
                    temp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = temp
                    # then, move the index i (current) to the next right child node
                    i = 2 * i + 1
                
                # elif there's only a left node, and left node < node at i, swap that node with node at i (current node) 
                elif self.heap[ 2 * i] < self.heap[i]: 
                    # swap the 2 nodes: 
                    temp = self.heap[i] 
                    self.heap[i] = self.heap[ 2 * i]
                    self.heap[ 2 * i] = temp
                    # move the index i to the next left child 
                    i = 2 * i 

                # else, if current node < left and < right child node, break out of the loop
                else: 
                    break 
            
            # get to the next current index to keep going into the while loop above, to 
            # keep percolate down until the tree attain its order property 
            current -= 1

