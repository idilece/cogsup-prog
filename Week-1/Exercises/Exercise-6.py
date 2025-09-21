"""
Write a script that lists all the prime numbers between 1 and 10000.
(A prime number is an integer greater or equal to 2 which has no divisors except 1 and itself). 
Hint: Write an is_factor helper function.
"""

import math

def is_factor(d, n):
    """True iff (if and only if) d is a divisor of n."""
    return n % d == 0
    pass

def is_prime(n):
    if n < 2:
        return False
    
    for d in range(2, int(math.sqrt(n)) + 1):
        if is_factor(d, n):
            return False 
        
    return True 

    pass

list_of_primes = []

for prime_num in range(1, 10001):   
    if is_prime(prime_num):         
        list_of_primes.append(prime_num)  

print(list_of_primes)





