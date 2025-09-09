
# Project Euler problem 32: pandigital products

import math

def compute(): # I limit the search
	ans = sum(i for i in range(1, 10000) if has_pandigital_product(i))
	return str(ans)

def has_pandigital_product(n): # Checking if n can be a pandigital product
	for i in range(1, math.isqrt(n) + 1):
		if n % i == 0:
			temp = str(n) + str(i) + str(n // i)
			if "".join(sorted(temp)) == "123456789":
				return True
	return False

if __name__ == "__main__":
	print(compute())