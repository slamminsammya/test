import itertools
import math

def gcd(a,b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

def isprime(n):
    primes = [2,3,5]
    if n <6:
        return n in primes
    else:
        if n%2 == 0:
            return false
        bound = int(math.floor(math.sqrt(n)))
        for x in range(3, bound + 1, 2):
            if isprime(x) and n%x == 0:
                return False
        return True

