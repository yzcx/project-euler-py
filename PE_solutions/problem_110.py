
# Project Euler problem 110: diophantine reciprocals II

REQUIRED_TAU_SQUARED = 8000001
PRIME_FACTORS = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

MIN_N = float('inf')

def find_min_n(tau_val, n_val, prime_index, max_exp): # Recursive DFS to find minimal n
    global MIN_N
    if n_val >= MIN_N: # Pruning, if current n is too large stop branch
        return
    if tau_val >= REQUIRED_TAU_SQUARED: # Base case 1, solution found
        MIN_N = min(MIN_N, n_val)
        return
    if prime_index >= len(PRIME_FACTORS): # Base case 2, ran out of primes to use
        return

    p = PRIME_FACTORS[prime_index]
    current_n_val = n_val
    current_tau_val = tau_val

    for e in range(max_exp + 1): # Iterate through possible exponents e
        if e > 0:
            current_n_val *= p
            current_tau_val = tau_val * (2 * e + 1)
        if current_tau_val >= REQUIRED_TAU_SQUARED:
            MIN_N = min(MIN_N, current_n_val)
            break
        if current_n_val < MIN_N: # Recurse, move to next prime, passing current exponent e as new limit
            find_min_n(current_tau_val, current_n_val, prime_index + 1, e)

def compute():
    global MIN_N
    find_min_n(1, 1, 0, 30) # DFS
    return str(int(MIN_N))

if __name__ == "__main__":
    print(compute())