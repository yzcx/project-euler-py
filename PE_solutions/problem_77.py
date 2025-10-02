
# Project Euler problem 77: prime summations

import math

def prime_sieve(limit):
    is_prime = [True] * (limit + 1) # Forming a list for Sieve of Eratosthenes
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i, is_p in enumerate(is_prime) if is_p]

def compute():
    TARGET_WAYS = 5000
    MAX_N_CHECK = 100 # Max num to check in DP table

    primes = prime_sieve(MAX_N_CHECK)

    ways = [1] + [0] * MAX_N_CHECK # Number of ways to sum to i

    for p in primes: # Iterate through each prime and update ways arrays
        for i in range(p, MAX_N_CHECK + 1):
            ways[i] += ways[i - p]

    for n in range(2, MAX_N_CHECK + 1): # Searching DP table for first number that exceeds target
        if ways[n] > TARGET_WAYS:
            return str(n)

if __name__ == "__main__":
    print(compute())