
# Project Euler problem 51: prime digit replacements

def list_primality(n): # Sieve of Eratosthenes to get list of primes fast
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, n + 1, i):
                is_prime[multiple] = False
    return is_prime

def do_mask(digits, mask): # Template of number
    return [d * ((~mask >> i) & 1) for (i, d) in enumerate(digits)]

def add_mask(digits, mask): # Replacement digit
    return [d + ((mask >> i) & 1) for (i, d) in enumerate(digits)]

def to_number(digits): # Converts list of digits back into integer
    result = 0
    for d in digits:
        result = result * 10 + d
    return result

def compute():
    isprime = list_primality(1000000)

    for i in range(len(isprime)):
        if not isprime[i]:
            continue

        n = [int(c) for c in str(i)]

        for mask in range(1 << len(n)): # Bitmask to check all possible combos of digits to replace
            digits = do_mask(n, mask)
            count = 0

            for j in range(10):
                if digits[0] != 0 and isprime[to_number(digits)]:
                    count += 1
                digits = add_mask(digits, mask)

            if count == 8:
                digits = do_mask(n, mask)
                for j in range(10):
                    if digits[0] != 0 and isprime[to_number(digits)]:
                        return str(to_number(digits))
                    digits = add_mask(digits, mask)
    raise AssertionError("Not found")

if __name__ == "__main__":
    print(compute())