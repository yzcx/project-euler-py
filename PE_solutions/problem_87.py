
# Project Euler problem 87: prime power triples

import math

def list_primes(limit): # Helper function, Sieve of Eratosthenes for prime generation
    if limit < 2: return []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i, is_p in enumerate(is_prime) if is_p]

def compute():
    LIMIT = 50000000

    primes = list_primes(math.isqrt(LIMIT))

    sums = {0}

    for i in range(2, 5): # Iterate through exponents
        newsums = set()
        for p in primes: # Iterate over all primes as base for current power
            q = p ** i
            if q > LIMIT:
                break
            for x in sums: # Combine current power with all previously found partial sums
                if x + q <= LIMIT:
                    newsums.add(x + q)
        sums = newsums
    return str(len(sums))

if __name__ == "__main__":
    print(compute())