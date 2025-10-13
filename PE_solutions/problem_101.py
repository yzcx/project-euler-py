
# Project Euler problem 101: optimum polynomial

from fractions import Fraction

def generating_function(n):
    return sum((-n) ** i for i in range(11))

def optimum_polynomial(k, n): # Calculates value of OP via lagrange interpolation
    s = Fraction(0, 1)
    for j in range(1, k + 1): # Loop through k data points used for interpolation
        p = Fraction(generating_function(j), 1)
        for i in range(1, k + 1):
            if i != j:
                p *= Fraction(n - i, j - i)
        s += p
    return s

def compute():
    ans = Fraction(0, 1)
    for k in range(1, 11):
        term = optimum_polynomial(k, k + 1)
        ans += term
    return str(ans.numerator)

if __name__ == "__main__":
    print(compute())