
# Project Euler problem 58: spiral primes

import fractions, itertools

def is_prime(n): # To check if number is prime
    if n < 2: # Handling small numbers first and then checking for divisibility only by numbers up to square root
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def compute():
    TARGET = fractions.Fraction(1, 10)
    numprimes = 0
    for n in itertools.count(1, 2): # Generating odd numbers for side length of spiral
        for i in range(4): # New layer of spiral adds 4 numbers to diagonals, I check each of those numbers for primality
            if n > 1 and is_prime(n * n - i * (n - 1)): # My thinking is I can get these numbers without building the whole spiral
                numprimes += 1
        if n > 1 and fractions.Fraction(numprimes, n * 2 - 1) < TARGET:
            return str(n)

if __name__ == "__main__":
    print(compute())