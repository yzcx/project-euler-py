
# Project Euler problem 41: pandigital prime

import itertools

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def solve(): # Using math trick to rule out most pandigital numbers
    for n in [7, 4, 1]:
        digits = list(range(1, n + 1))
        permutations = [int("".join(map(str, p))) for p in itertools.permutations(digits)] # Generates permutations of digits
        permutations.sort(reverse=True)
        for num in permutations:
            if is_prime(num):
                return str(num)
    return "No solution found"

if __name__ == "__main__":
    print(solve())