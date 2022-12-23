# INSERTION SORT
# Time complexity: Best: O(n), worst: O(n^2)
def insertionSort(array): 
    # Traverse through 1 to len(array) 
    for i in range (1,len(array)):
        j = i - 1
        while j >= 0 and array[j + 1] < array[j]: 
            # array[j+1] and array[j] are out of order so swap them
            temp = array[j+1]
            array[j+1] = array[j] 
            array[j] = temp 
            j -= 1
    return array 

