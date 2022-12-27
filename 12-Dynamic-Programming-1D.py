'''
Example of a 1D DP problem, looking at fibonacci number
F(n) = F(n-1) + F(n-2)  (base case, F1, F0)

Example: 
                        F(5)
            F(4)                        F(3)
        F(3)         F(2)          F(2)     F(1)
    F(2)   F(1)   F(1)  F(0)     F(1)  F(0)
F(1)  F(0)
                                    
'''

# Method 1. Solve using RECURSION (not as efficient) 
def fib_bruteforce(n):
    if n <= 1: 
        return n
    return fib_bruteforce(n-1) + fib_bruteforce(n-2)

# Method 2. MEMOIZATION or TOP-DOWN DYNAMIC PROGRAMMING
# Use hashmap to represent the cache, cache(3) will be remembered for
# the right sub-tree when we get to it, therefore reduce time complexity
# as program doesn't have to repeatedly calculate the recursive F(3), F(2) again

def memoization(n, cache): 
    if n <= 1: 
        return n
    if n in cache: 
        return cache[n]
    
    # cache formula: 
    cache[n] = memoization(n - 1) + memoization(n - 2) 
    return cache[n] 

# Method 3. (considered as TRUE DP technique) or BOTTOM-UP DP
def dp(n): 
    if n < 2: 
        return n
    
    dp = [0, 1]

    # start at 2 and calculate the next F(n) 
    i = 2
    while i <= n: 
        temp = dp[1]
        dp[1] = dp[0] + dp[1]
        dp[0] = temp
        i += 1
    return dp[1] 
