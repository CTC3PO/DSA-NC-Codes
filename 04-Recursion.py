# FACTORIAL 
# recursive implementation of n! (n-factorial) calculation
# this is a 1-branch recursion

def factorial(n):
    # base case
    if n <= 1: 
        return 1
    #recursive case:
    return n * factorial(n-1)

#TIME COMPLEXITY of factorial
    # O(n) 

#FIBONACCI 
# F(n) = F(n-1) + F(n-2) (where F(1) = 1, F(0) = 0)
# this is a 2-branch 
#TIME COMPLEXITY 
    # O (2^n) - not very efficient   
    # everytime traverse down 1 level/height of tree:
    # it branches out to 2 branches until reaching the base case
    # so 2^n (n is the number of level, and n in F(n) )
    
''' example: 
                F(4)
        F(3)              F(2)      (branches double everytime goes down 1 level) 
    F(2)      F(1)     F(1)   F(0)  (base case) 
F(1)  F(0) (base case)              (there's n level)
''' 

def fibonacci(n):
    # base case: 
    if n <=1 : 
        return n
    return fibonacci (n-1) + fibonacci(n-2)



