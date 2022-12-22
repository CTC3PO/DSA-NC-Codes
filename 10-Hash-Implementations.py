#INITIALIZE PAIR (key, value): 
class Pair: 
    def __init__(self, key, val):
        self.key = key
        self.val = val

#INITIALIZE Hashmap: 
class HashMap: 
    def __init__(self):
        self.size = 0
        self.capacity = 2
        self. map = [None, None]
    
    # Hash function (ord is func to convert ascii character to a value):
    def hash (self, key):
        index = 0
        # adding all the characters' converted value
        # to index and mod it for capacity
        for c in key: 
            index += ord(c)
        return index % self.capacity
    
    # Get function
    def get (self, key):
        #first, hash the key 
        index = self.hash(key)

        # try to find the key,value pair if index exists: 
        while self.map[index] != None: 
            if self.map[index].key == key: 
                return self.map[index].val
            # if can't find, increase the index and mod it for
            # capacity to get to next index
            index += 1
            index = index % self.capacity
        
    # PUT function
    def put (self, key, val): 
        index = self.hash(key)

        while True: 
            # if index doesn't exists, put key,value pair there            
            if self.map[index] == None: 
                self.map[index] = Pair(key,val)
                # increase size by 1, and rehash table if size becoming large
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return

            # if key,value pair exists, update the value at that key
            elif self.map[index].key == key: 
                self.map[index].val = val
                return

            #otherwise, increase index +1 and get the next index 
            index += 1
            index = index % self.capacity

    # REMOVE function: 
    def remove (self,key):
        if not self.get(key): 
            return 

        index = self.hash(key) 
        while True: 
            if self.map[index].key == key: 
                # Removing an element using open-addressing actually causes a bug,
                # because we may create a hole in the list, and our get() may
                # stop searching early when it reaches this hole.
                self.map[index] = None
                self.size -= 1
                return 
            index += 1
            index = index % self.capacity

    # REHASH function (when size >= capacity/2) 
    def rehash(self):
        self.capacity = 2 * self.capacity
        newMap = []
        for i in range(self.capacity):
            newMap.append[None]

        # copy current old map to oldMap array and set current map as newMap
        # then copy elements to the newMap array
        oldMap = self.map
        self.map = newMap
        self.size = 0
        for pair in oldMap: 
            if pair: 
                self.put(pair.key, pair.val) 

    #Print out key,value pair
    def print(self):
        for pair in self.map:
            if pair: 
                print(pair.key, pair.val) 
