import heapq

# for MIN HEAP

class Heap: 

    # function: Heapify:
    def heapify(self, arr):
        # move 0-th position to the end:
        arr.append(arr[0])

        # assign the array as heap
        self.heap = arr

        #get the current index (which is the first node with children)
        # we skip over the last half of the nodes (since they don't have children)
        current = (len(self.heap) - 1) // 2
        while current > 0: 
            #Percolate down: 
            i = current

            while 2 * i < len (self.heap): 
                if (2 * i + 1 < len(self.heap) and 
                self.heap [2 * i + 1] < self.heap[2 * i] and
                self.heap [2 * i + 1] < self.heap[i]):
                    # Swap right child: 
                    temp = self.heap[i]
                    self.heap[i] = self.heap[2 * i +1]
                    self.heap[2 * i +1] = temp
                    i = 2 * i + 1
                elif self.heap[i] > self.heap[2*i]:
                    # Swap left child:
                    temp = self.heap[i]
                    self.heap[i] = self.heap [2 * i] 
                    self.heap[2 * i] = temp
                    i = 2 * i
                else: 
                    break
            current -=1
