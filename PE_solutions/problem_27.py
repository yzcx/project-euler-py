
# Project Euler problem 27: quadratic primes

import itertools

def is_this_prime(number): # I create a function that quickly checks if a number is prime
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_the_best_pair(): # The plan is to track the longest streak of primes and the product that made it
    max_primes_found = 0
    the_product = 0

    for a in range(-999, 1000):
        for b in range(2, 1001):
            if is_this_prime(b):
                current_primes = 0
                for n in itertools.count():
                    val = n ** 2 + a * n + b
                    if is_this_prime(val):
                        current_primes += 1
                    else:
                        break

                if current_primes > max_primes_found:
                    max_primes_found = current_primes
                    the_product = a * b
    return str(the_product)

if __name__ == "__main__":
    print(find_the_best_pair())