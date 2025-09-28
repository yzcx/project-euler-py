
# Project Euler problem 69: totient maximum

import fractions

def list_totients(limit): # Implementing Euler's totient sieve to calculate phi(n) for all n up to the limit
    phi = list(range(limit + 1))
    for i in range(2, limit + 1):
        if phi[i] == i:
            for j in range(i, limit + 1, i):
                phi[j] -= phi[j] // i
    return phi

def compute():
    totients = list_totients(10 ** 6) # Calc all totient values up to 1 mil
    ans = max(range(2, len(totients)), key=(lambda i: fractions.Fraction(i, totients[i]))) # Max function iterates through all nums and uses lambda to compare exact fraction
    return str(ans)

if __name__ == "__main__":
    print(compute())