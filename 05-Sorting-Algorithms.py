# INSERTION SORT
# Time complexity: Best: O(n), worst: O(n^2)
# Insertion sort is a STABLE SORT (it preserves the original position of a number,
# for example: 7 7 3 will be preserved as 3 7 7 (where the first 7 shows up first
# in the sort before the other 7))
def insertionSort(array): 
    # Traverse through 1 to len(array) 
    for i in range ( 1, len(array) ):
        j = i - 1
        while j >= 0 and array[j + 1] < array[j]: 
            # array[j+1] and array[j] are out of order so swap them
            temp = array[j+1]
            array[j+1] = array[j] 
            array[j] = temp 
            j -= 1
    return array 

# MERGE SORT
# 2 -branch recursion 
# keep splitting the aray in half until reaching base case (<=1 element array,
# , meaning: end index - start index + 1 <= 1 )
# sort left array, sort right array, then merge in place using 2 pointer technique 
# TIME COMPLEXITY: O(n.logn) - where n is the number of levels (has to sort each lv
# and log(n) represents how many time we have to divide by 2 to get 
# to the base case)

def mergeSort(arr, s, e):
    if e - s + 1 <= 1: 
        return arr
    
    # get the middle array 
    m = (s + e) / 2

    # sort the left and irhgt half (recursion)
    mergeSort(arr, s, m)
    mergeSort(arr, m + 1, e)

    #merge back the sorted L and R halfs
    merge(arr, s, m, e)
    return arr

# MERGE IN PLACE (helper function) 
def merge(arr, s, m, e): 
    # Copying the sorted halfs to temp arrays
    L = arr[s : m + 1]
    R = arr[m + 1, e + 1]

    # assign starting index for L and R halfs and original arr
    i = 0   #index for L
    j = 0   #index for R
    k = s   #index for original arr (s: starting index)

    # Merge the 2 sorted halfs to the original array
    while i < len(L) and j < len(R):
        # compare the 2 halfs value and copy the lesser one to the arr
        if L[i] < R[j]:    
            arr[k] = L[i]
            i += 1
        else: 
            arr[k] = R[j]
            j += 1
        #increment original array index
        k += 1
    
    # One of the halfs will have elements remaining
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


# QUICKSORT
# 2 -branch recursion 
# pick the pivot (usually the right most value) and compare it
# to each elements on the left of it, if less than, move 
# that element at position of the left pointer
# this is sorted in place (no need to create new array),
# unlike Merge sort
# TIME COMPLEXITY: average: O(n*logn), worst: O(n^2) 

def quickSort(arr, s, e):
    # return original array if array has <= 1 element
    if e - s + 1 <= 1: 
        return arr

    # get the 2 pointers: 1 for left and another for the pivot
    pivot = arr[e]   #pivot is the last element of arr
    left = s    # pointer for left side

    # partition: elements <= pivot goes to    
    # the left side, elements > pivot to the right.
    for i in range (s,e): 
        if arr[i] < pivot: 
            temp = arr[left] 
            arr[left] = arr[i]
            arr[i] = temp
            left += 1

    # Move the pivot in-between left and right sides
    arr[e] = arr[left]
    arr[left] = pivot

    # then call quickSort again (recursion) on the left and right arrays
    quickSort(arr, s, left - 1)
    quickSort(arr, left + 1, e)

    return arr 

# BUCKET SORT 
# ONLY use when input where values within some specified range
# counts how many times each value appear, then put them back
# in the original array n times 

def bucketSort (arr):
    # Assume in this examples, arr only contains value 0,1,2
    # initialize the counts array, set count to 0
    counts = [0,0,0]

    # Count the quantity of each value in arr: 
    for n in arr: 
        counts[n] += 1

    # Fill the original array with the values * how many times the value appear
    i = 0
    for n in range (len(counts)):
        for j in range (counts[n]):
            arr[i] = n
            i += 1
    return arr
