# HASH IMPLEMENTATION
# when hash map half full, we double it (2x), then REHASH the array, we have to recomputer the hash (index)
# and move the elments to its new position. 

# example: add alice to index 1, 25 % 2 = 1, 
# add brad (size doubles to 4), now brad 27 % 4 = 3, add
# brad to 3rd index. Then add collin, have ot double size, 
# then get collin = 33 % 8 = 1, now collin position collides
# with alice at index 1 ===> we use OPEN ADDRESSING (add collin
# to the next available position next to 1, meaning 2)
# but this is not the best way (+1 for collin) for open addressing
# there's more way to configure this. Array size to be a prim
# number to be more optimal - double the size to roughly to be 
# prime number sized array 
''' INSERT      REMOVE      SEARCH
    O(1)        O(1)        O(1) '''

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
    
    # Hash function (ord in python is function to convert ascii
    # character to a value):
    # Hash is to take index value and mod by capacity to get the remainder
    def hash (self, key):
        index = 0
        # adding all the characters' converted value
        # to index and mod it for capacity
        for c in key: 
            index += ord(c)
        return index % self.capacity
    
    # SEARCH / Get function
    # keep searching for the key, val pair, rehash the index by +1 and 
    # then mod for capacity, if found the key, return its value,
    # do this until reaching a place with empty index, if not 
    # found, return None
    def get (self, key):
        #first, hash the key 
        index = self.hash(key)

        # try to find the key,value pair if index exists: 
        while self.map[index] != None: 
            if self.map[index].key == key: 
                return self.map[index].val
            # if can't find, increase the index and mod it for
            # capacity to get to next index, then enter the while loop again
            index += 1
            index = index % self.capacity

        return None
        
    # PUT function
    # Put function adds a new key, value pair to the index if there's nothing
    # yet at that index, or update the value of the key if there's already 
    # a key,value pair at that index. When adding new key,val pair, increase
    # the size by 1 and double the size if size is half of capacity 
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

            # otherwise, increase index +1 and hash to get the next index,
            index += 1
            index = index % self.capacity

    # REMOVE function: 
    def remove (self,key):
        # if key doesn't exist, return nothing
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
