def binarySearchWithRange(low, high):
    while low < high:
        mid = (low + high) /2

        #check isCorrect condition for mid
        # then move high or low accordingly
        if isCorrect(mid) > 0:
            high = mid -1
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

