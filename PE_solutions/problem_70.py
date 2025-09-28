
# Project Euler problem 70: totient permutation

def list_totients(limit): # Implementing Euler's totient sieve to calculate phi(n) for all n up to limit
    phi = list(range(limit + 1))

    for i in range(2, limit + 1):
        if phi[i] == i:
            for j in range(i, limit + 1, i): # Apply totient formula correction to all multiples of j of prime i
                phi[j] -= phi[j] // i
    return phi

def compute():
    LIMIT = 10 ** 7
    totients = list_totients(LIMIT - 1) # Calc all totient values up to limit using custom seive

    minnumer = 1
    mindenom = 0

    for (i, tot) in enumerate(totients[2:], 2): # Iterate through n(i) and its totient to find min. ratio
        if i * mindenom < minnumer * tot and sorted(str(i)) == sorted(str(tot)):
            minnumer = i
            mindenom = tot
    return str(minnumer)

if __name__ == "__main__":
    print(compute())