# Python array are dynamic by default, but this is an example of resizing

class Array: 
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.arr = [0] * 2  #array of capacity = 2
    
    # INSERT LAST
    # insert n at last position of the array
    def insertLast(self, n):
        # check if length = capcity, if so, resize array's capacity
        if self.length == self.capacity: 
            self.resize()
        #insert at next empty position and increase length by 1
        self.arr[self.length] = n
        self.length +=1 
    
    # RESIZE (helper function) 
    # create and copy all elements to the new array
    def resize(self):
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity

        # copy elements over: 
        for i in range (self.length): 
            newArr[i] = self.arr[i]
        #set the new array as the array
        self.arr = newArr

    # REMOVE LAST
    # remove last element of the array
    # by checking if there's anything to remove first (array length >0)
    # then pop out last value by reducing the array's length by 1
    def removeLast(self):
        if self.length > 0:
            self.length -= 1
    
    # GET value at index i
    def get(self, i):
        if i < self.length: 
            return self.arr[i]
        # here we would throw an out of bounds exception

    # INSERT value at index i: 
    def insert(self, i, n):
        if i < self.length: 
            self.arr[i] = n
            return
        # Here we would throw an out of bounds exception

    # PRINT
    def printArray(self):
        for i in range (self.length):
            print(self.arr[i])
        print() 
        