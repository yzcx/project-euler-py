
# Project Euler problem 104: pandigital fibonacci ends

import math

def is_pandigital(n_str):
    return len(n_str) == 9 and '0' not in n_str and len(set(n_str)) == 9

def compute():
    MOD = 10 ** 9 # Modulus for finding last 9 digits
    PHI_LOG10 = math.log10((1 + math.sqrt(5)) / 2) # Logarithmic constants for approximating first 9 digits
    SQRT5_LOG10 = math.log10(math.sqrt(5))

    f_a = 1
    f_b = 1
    k = 2

    while True:
        k += 1
        f_next_tail = (f_a + f_b) % MOD # Calculate next Fibonacci number's tail using modular arithmetic
        f_a = f_b
        f_b = f_next_tail
        if is_pandigital(str(f_b)): # Check pandigital property for last 9 digits
            log_fk = k * PHI_LOG10 - SQRT5_LOG10
            frac_part = log_fk - math.floor(log_fk)
            first_nine_digits = int(10 ** 8 * 10 ** frac_part)
            if is_pandigital(str(first_nine_digits)): # Check pandigital property for first 9 digits
                return str(k)

if __name__ == "__main__":
    print(compute())