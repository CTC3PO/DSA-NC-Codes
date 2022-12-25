# HASH TIME COMPLEXITY: 
''' INSERT      REMOVE      SEARCH
    O(1)        O(1)        O(1) '''

# HASHMAP can't contain duplicantes 

#Example code in Python (Java and other languages have a built in hashmap)
names = ["alice", "brad", "collin", "brad", "dylan", "kim"]

# initialize a counmap 
countMap = {}

for name in names:
    if name not in countMap:
        countMap[name] = 1
    else: 
        countMap[name] += 1