# INSERT AT END
# insert n into array at the next open position (end)
#length (number of "real" values in array)
#capacity (size or memory allocated for the fixed size array) 

def insertEnd(array, n, length, capacity):
    if length < capacity:
        array[length] = n

# REMOVE AT END
# REMOVE the last position of the array (if the 
# array is not empty)
def removeEnd(array, length):
    if length >0:
        # overwrite last element with default value
        # also decrease the length by 1
        array[length - 1] = 0

#INSERT MIDDLE
# insert n into index i of the array, shifting
# array elements to the right
def insertMiddle(array, i, n, length):
    # shift starting from the end to i: 
    for index in range (length - 1, i - 1, -1):
        array[index+1] = array[index]

    #insert at i
    array[i] = n 

# REMOVE MIDDLE
# remove an element at i index, shift the 
# array elements to the left
def removeMiddle(array, i, length):
    #shift starting from i+1 to end:
    for index in range(i+1, length):
        array[index-1] = array[index]
    
#PRINTING array
def printArray(array, capacity):
    for i in range (capacity):
        print(array[i])