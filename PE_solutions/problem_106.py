
# Project Euler problem 106: special subset sums meta testing

import math

def compute():
    SET_SIZE = 12

    def catalan(n): # Helper function to compute nth catalan number
        return math.comb(n * 2, n) // (n + 1)

    ans = sum(math.comb(SET_SIZE, i * 2) * (math.comb(i * 2, i) // 2 - catalan(i))
              for i in range(2, SET_SIZE // 2 + 1))
    return str(ans)

if __name__ == "__main__":
    print(compute())