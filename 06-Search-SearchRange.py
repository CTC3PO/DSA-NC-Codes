#Implementation of binary search
# TIME COMPLEXITY: O(logn) - because we eliminate/narrow down
# to half the values each time (2^x = n, so x = logn)

def binarySearch(arr, target):
    L,R = 0, len(arr) - 1

    while L <= R:
        mid = (L + R) // 2

        if target > arr[mid]:
            L = mid + 1
        elif target < arr[mid]:
            R = mid - 1
        else: 
            return mid
    # Return -1 if found no target (target not in array)
    return -1   

def binarySearchWithRange(low, high):
    while low < high:
        mid = (low + high) /2

        #check isCorrect condition for mid
        # then move high or low accordingly
        if isCorrect(mid) > 0:
            high = mid - 1
        elif isCorrect(mid) < 0:
            low = mid + 1
        else: 
            return mid
        return -1 

#this helper function checks if the guessed number (to find) is 
# > or < the target number. if less than, return -1 , if more, return +1
def isCorrect(num): 
    if num > 10:
        return 1
    elif num < 10: 
        return -1
    else: return 0

