
# Project Euler problem 53: combinatoric selections

import math

def compute(): # Checking every possible combo for n and k and count ones that are bigger than a million, nested generator expressions does this quick
	ans = sum(1
		for n in range(1, 101)
		for k in range(0, n + 1)
		if math.comb(n, k) > 1000000)
	return str(ans)

if __name__ == "__main__":
	print(compute())