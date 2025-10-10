
# Project Euler problem 94: almost equilateral triangles

import math, itertools

def compute():
	LIMIT = 10**9
	ans = 0

	for s in itertools.count(1, 2): # Iterate over parameter s
		if s * s > (LIMIT + 1) // 3:
			break
		for t in range(s - 2, 0, -2): # Iterate over parameter t. s and t must be odd and coprime
			if math.gcd(s, t) == 1: # Checking for coprimality, ensures generated triple is primitive
				a = s * t
				b = (s * s - t * t) // 2
				c = (s * s + t * t) // 2
				if a * 2 == c - 1: # Condition 1
					p = c * 3 - 1
					if p <= LIMIT:
						ans += p
				if a * 2 == c + 1: # Condition 2
					p = c * 3 + 1
					if p <= LIMIT:
						ans += p
				if b * 2 == c - 1: # Condition 3
					p = c * 3 - 1
					if p <= LIMIT:
						ans += p
				if b * 2 == c + 1: # Condition 4
					p = c * 3 + 1
					if p <= LIMIT:
						ans += p
	return str(ans)

if __name__ == "__main__":
	print(compute())