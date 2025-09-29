
# Project Euler problem 72: counting fractions

def list_totients(limit):
    phi = list(range(limit + 1))

    for i in range(2, limit + 1):
        if phi[i] == i:
            for j in range(i, limit + 1, i): # For all multiples j of prime i, apply totient formula correction
                phi[j] -= phi[j] // i
    return phi

def compute():
    LIMIT = 10 ** 6 # Max denom
    totients = list_totients(LIMIT) # Generates all totient values up to limit

    ans = sum(totients[2:])# Total num of reduces proper fractions is sum of phi(d) for d=2 to LIMIT
    return str(ans)

if __name__ == "__main__":
    print(compute())