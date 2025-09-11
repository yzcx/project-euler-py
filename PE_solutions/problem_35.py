
# Project Euler problem 35: circular primes

import itertools

def list_primality(n): # Sieve of Eratosthenes which finds all prime numbers
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, n + 1, i):
                is_prime[multiple] = False
    return is_prime

def compute():
    limit = 1000000
    isprime = list_primality(limit - 1)

    def is_circular_prime(n):
        s = str(n)
        return all(isprime[int(s[i:] + s[:i])] for i in range(len(s)))

    ans = sum(1 # Counting all numbers that are both prime and circular
              for i in itertools.compress(range(len(isprime)), isprime)
              if is_circular_prime(i))
    return str(ans)

if __name__ == "__main__":
    print(compute())
