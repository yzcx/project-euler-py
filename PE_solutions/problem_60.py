
# Project Euler problem 60: prime pair sets

import functools, math

def list_primes(limit): # Generates list of primes up to given limit using a seive
    if limit < 2:
        return []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
    primes = [p for p, is_p in enumerate(is_prime) if is_p]
    return primes

def compute():
    PRIME_LIMIT = 100000 # Setting an UB for primes to check
    primes = list_primes(PRIME_LIMIT)

    def find_set_sum(prefix, targetsize, sumlimit): # Recursive function searching for a set of primes with desired property
        if len(prefix) == targetsize: # Base case is if the set has the target size, return its sum
            return sum(primes[i] for i in prefix)
        else: # Determines where to start searching for next prime to add to set
            istart = 0 if (len(prefix) == 0) else (prefix[-1] + 1)
            for i in range(istart, len(primes)):
                if primes[i] > sumlimit:
                    break
                if all((is_concat_prime(i, j) and is_concat_prime(j, i)) for j in prefix): # Checking if current prime can be concatenated
                    prefix.append(i)
                    result = find_set_sum(prefix, targetsize, sumlimit - primes[i])
                    prefix.pop()
                    if result is not None:
                        return result
            return None

    @functools.cache
    def is_concat_prime(x, y):
        return is_prime(int(str(primes[x]) + str(primes[y])))

    def is_prime(x): # Helper function to check if number is prime
        if x < 0:
            raise ValueError()
        elif x in (0, 1):
            return False
        else:
            end = math.isqrt(x)
            for p in primes:
                if p > end:
                    break
                if x % p == 0:
                    return False
            for i in range(primes[-1] + 2, end + 1, 2):
                if x % i == 0:
                    return False
            return True

    sumlimit = PRIME_LIMIT # Loop that drives the search
    while True:
        setsum = find_set_sum([], 5, sumlimit - 1)
        if setsum is None:
            return str(sumlimit)
        sumlimit = setsum

if __name__ == "__main__":
    print(compute())