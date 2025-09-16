
# Project Euler problem 46: goldbach's other conjecture

import itertools

def is_prime(n): # Creating a function checking for primality
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def compute(): # Starts checking from 9
    ans = next(itertools.filterfalse(test_goldbach, itertools.count(9, 2)))
    return str(ans)

def test_goldbach(n): # To check if number satisfies Goldbach's conjecture
    if n % 2 == 0 or is_prime(n):
        return True
    for i in itertools.count(1):
        k = n - 2 * i * i
        if k <= 0:
            return False
        elif is_prime(k):
            return True

if __name__ == "__main__":
    print(compute())