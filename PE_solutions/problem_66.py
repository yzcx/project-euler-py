
# Project Euler problem 66: diophantine equation

import fractions, math

def is_square(n): # Checking if number is square
    if n < 0:
        return False
    if n == 0:
        return True
    sqrt_n = int(math.isqrt(n))
    return sqrt_n * sqrt_n == n

def smallest_solution_x(n): # Returns smallest x for a given non square D
    contfrac = sqrt_to_continued_fraction(n)
    temp = contfrac[0] + contfrac[1][: -1]

    val = fractions.Fraction(temp[-1], 1) # Calculates convergent from the terms in 'temp' by working backwards
    for term in reversed(temp[: -1]):
        val = 1 / val + term

    if len(contfrac[1]) % 2 == 0: # Checking length of the period to determine which formula to use
        return val.numerator
    else:
        return val.numerator ** 2 + val.denominator ** 2 * n

def sqrt_to_continued_fraction(n): # Returns continued fraction expansion of sqrt(n) and its period
    terms = []
    seen = {}
    val = QuadraticSurd(0, 1, 1, n)
    while True:
        seen[val] = len(seen)
        flr = val.floor()
        terms.append(flr)
        val = (val - QuadraticSurd(flr, 0, 1, val.d)).reciprocal()
        if val in seen:
            break
    split = seen[val]
    return (terms[: split], terms[split:])

class QuadraticSurd:
    def __init__(self, a, b, c, d):
        if c == 0:
            raise ValueError()

        if c < 0: # Simplify fraction by dividing GCD
            a = -a
            b = -b
            c = -c
        gcd = math.gcd(a, b, c)
        if gcd != 1:
            a //= gcd
            b //= gcd
            c //= gcd

        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __sub__(self, other):
        if self.d != other.d:
            raise ValueError()
        return QuadraticSurd(
            self.a * other.c - other.a * self.c,
            self.b * other.c - other.b * self.c,
            self.c * other.c,
            self.d)

    def reciprocal(self):
        return QuadraticSurd(
            -self.a * self.c,
            self.b * self.c,
            self.b * self.b * self.d - self.a * self.a,
            self.d)

    def floor(self): # Finds integer part of quadratic surd
        temp = math.isqrt(self.b * self.b * self.d)
        if self.b < 0:
            temp = -(temp + 1)
        temp += self.a
        if temp < 0:
            temp -= self.c - 1
        return temp // self.c

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b \
            and self.c == other.c and self.d == other.d

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash(self.a) + hash(self.b) + hash(self.c) + hash(self.d)

def compute():
    ans = max((n for n in range(2, 1001) if (not is_square(n))), key=smallest_solution_x)
    return str(ans)

if __name__ == "__main__":
    print(compute())