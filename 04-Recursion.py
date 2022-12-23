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
# F(n) = F(n-1) + F(n-2) (F(1) = 1, F(0) = 0)
# this is a 2-branch recursion

def fibonacci(n):
    # base case: 
    if n <=1 : 
        return n
    return fibonacci (n-1) + fibonacci(n-2)

#TIME COMPLEXITY of fibonacci: 
    # O (2^n) - not very efficient   
    # everytime traverse down 1 level/height of tree:
    # it branches out to 2 branches until reaching the base case
    # it's 2 to the n (n is the number of level, or n in F(n) )