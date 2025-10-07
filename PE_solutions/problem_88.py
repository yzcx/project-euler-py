
# Project Euler problem 88: product-sum numbers

def compute():
    LIMIT = 12000
    minsumproduct = [None] * (LIMIT + 1)

    def factorise(n, remain, maxfactor, sum, terms): # Recursive function to explore factorisations of n
        if remain == 1:
            if sum > n:
                raise AssertionError()
            terms += n - sum
            if terms <= LIMIT and (minsumproduct[terms] is None or n < minsumproduct[terms]): # If set size is within limit, update minimal product-sum number
                minsumproduct[terms] = n
        else:
            for i in range(2, maxfactor + 1): # Continue factorisation
                if remain % i == 0:
                    factor = i
                    factorise(n, remain // factor, min(factor, maxfactor), sum + factor, terms + 1)

    for i in range(2, LIMIT * 2 + 1): # Search loop
        factorise(i, i, i, 0, 0)

    ans = sum(set(minsumproduct[2:]))
    return str(ans)

if __name__ == "__main__":
    print(compute())