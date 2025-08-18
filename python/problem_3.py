
# Project Euler problem 3

from sympy.ntheory import primefactors # Using primefactors function from sympy library to find prime factors

ans = primefactors(600851475143)

print(ans)