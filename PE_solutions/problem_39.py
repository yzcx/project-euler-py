
# Project Euler problem 39: integer right triangles

def compute():
	ans = max(range(1, 1001), key=count_solutions) # Checking every possible perimeter within range
	return str(ans)

def count_solutions(p): # Counting how many right triangles exist for p
	result = 0
	for a in range(1, p + 1):
		for b in range(a, (p - a) // 2 + 1):
			c = p - a - b  # c >= b
			if a * a + b * b == c * c:
				result += 1
	return result

if __name__ == "__main__":
	print(compute())