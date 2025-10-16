
# Project Euler problem 108: diophantine reciprocals I

import itertools, math

def compute():
	for n in itertools.count(1):
		if (count_divisors_squared(n) + 1) // 2 > 1000:
			return str(n)

def count_divisors_squared(n): # Calculates using prime factorisation
	count = 1
	end = math.isqrt(n)
	for i in itertools.count(2): # Iterate through potential prime factors i of n
		if i > end:
			break
		if n % i == 0:
			j = 0 # j is exponent e of prime i in factorisation of n
			while True:
				n //= i
				j += 1
				if n % i != 0:
					break
			count *= j * 2 + 1
			end = math.isqrt(n)
	if n != 1:
		count *= 3
	return count

if __name__ == "__main__":
	print(compute())