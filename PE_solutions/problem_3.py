
# Project Euler problem 3: largest prime factor

from sympy.ntheory import primefactors # Using primefactors function from sympy library to find prime factors

ans = primefactors(600851475143)

print(ans)