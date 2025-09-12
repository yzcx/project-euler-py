
# Project Euler problem 37: truncatable primes

import itertools

def list_primality(n): # Creating a list of primes to search limit
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for multiple in range(i * i, n + 1, i):
                    is_prime[multiple] = False
        return is_prime

def is_truncatable_prime(n, is_prime_list): # Checking if prime is truncatable
        s = str(n)

        for i in range(1, len(s)):
            if not is_prime_list[int(s[i:])]:
                return False

        for i in range(1, len(s)):
            if not is_prime_list[int(s[:len(s) - i])]:
                return False

        return True

def compute(): # Logic to find sum
        limit = 1000000
        is_prime_list = list_primality(limit)

        ans = sum(itertools.islice(
            filter(lambda x: is_prime_list[x] and is_truncatable_prime(x, is_prime_list), itertools.count(10)), 11))
        return str(ans)

if __name__ == "__main__":
        print(compute())