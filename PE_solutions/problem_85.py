
# Project Euler problem 85: counting rectangles

import math

def compute():
	TARGET = 2000000
	end = math.isqrt(TARGET) + 1 # Determine search limit for grid dimensions. Setting a sufficient conservative UB for search as w and h does not need to be very large
	gen = ((w, h) for w in range(1, end) for h in range(1, end)) # Generate all pairs of grid dimensions
	func = lambda wh: abs(num_rectangles(*wh) - TARGET) # Lambda function to minimise, the absolute difference between the generated count and the TARGET
	ans = min(gen, key=func) # Finding pair that minimises the difference
	return str(ans[0] * ans[1])

def num_rectangles(m, n):
	return (m + 1) * m * (n + 1) * n // 4 # Formula for total num of rectangles in a m*n grid

if __name__ == "__main__":
	print(compute())