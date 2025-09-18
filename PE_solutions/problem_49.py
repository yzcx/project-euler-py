
# Project Euler problem 49: prime permutations

def list_primality(n): # Sieve of Eratosthenes function creates fast lookup list of all prime numbers
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, n + 1, i):
                is_prime[multiple] = False
    return is_prime

def has_same_digits(x, y): # Checks if two numbers have same digits
    return sorted(str(x)) == sorted(str(y))

def compute(): # Main logic
    limit = 10000
    isprime = list_primality(limit - 1)

    for base in range(1000, limit): # Looping through all 4 digit primes to use as first term
        if isprime[base]:
            for step in range(1, (limit - base) // 2 + 1):
                a = base + step
                b = a + step

                if a < limit and isprime[a] and has_same_digits(a, base) \
                        and b < limit and isprime[b] and has_same_digits(b, base) \
                        and (base != 1487 or a != 4817):
                    return str(base) + str(a) + str(b)

    print("Not found")

print(compute())