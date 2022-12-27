''' 
AND: n = 1 & 1

OR:  n = 1 & 0

XOR: n = 0 ^ 1

NOT: n = ~ n

TRUTH TABLE:

        | AND         OR          XOR
--------------------------------------
0 & 0   |  0           0           0
0 & 1   |  0           1           1
1 & 0   |  0           1           1
1 & 1   |  1           1           0

BIT SHIFTING: 
            n = 1
left:       n = n << 1 (same as * 2)
right:      n = n >> 1 (same as // 2)

n << 1 (shift left), every time shift to the left
equivalent to multiply by 2. everytime shift to the
right, equivalent to divided by 2 for example: 

    left          right 
001 ( x1)       100 ( //1)
010 ( x2)       010 ( //2)
100 ( x4)       001 ( //4)

'''

# COUNTING BITS 
# EXAMPLE: Count no of bits in 23 
# 23 is represented as 10111
# How to count bit of 23, we bitwise it 1 1 until it becomes 0
# it it bitwise with 1 evaluates to 1, increase count by 1

# (1)    10111  (no 23) 
#      & 00001  (no 1)
#       ----------------
#        00001 --> = 1 (increase count +1, count = 1) 

#        Shift RIGHT: 
# (2)    01011   
#      & 00001  (no 1)
#       ----------------
#        00001 --> = 1 (increase count +1, count = 2) 

#        Shift RIGHT: 
# (3)    00101  
#      & 00001  (no 1)
#       ----------------
#        00001 --> = 1 (increase count +1, count = 3) 

#        Shift RIGHT: 
# (4)    00010   
#      & 00001  (no 1)
#       ----------------
#        00001 --> = 0 ( count = 3) 

#        Shift RIGHT: 
# (5)    00001   
#      & 00001  (no 1)
#       ----------------
#        00001 --> = 1 (increase count +1, count = 4)
# 
# #        Shift RIGHT: 
# (6)    00000  --> n = 0 now, stop the while loop
# 
# Total count = 4  
#    

def countBits(n):
    count = 0

    # only enter the loop for n > 0 
    while n > 0:
        # we bitwise n with 1 (00001), if n and 1 
        # evaluates to 1, increase the count by 1
        if n & 1 == 1: 
            count += 1
        n = n >> 1  # shift n 1 bit to the right (same as // 2)
    
    return count 