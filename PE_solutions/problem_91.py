
# Project Euler problem 91: right triangles with integer coordinates

def compute():
	LIMIT = 51
	ans = sum(1 # Brute force through all possible two point combos
		for x1 in range(LIMIT)
		for y1 in range(LIMIT)
		for x2 in range(LIMIT)
		for y2 in range(LIMIT)
		if y2 * x1 < y1 * x2 and is_right_triangle(x1, y1, x2, y2)) # Filter, condition based on cross product ensures each unique triangle is only counted once
	return str(ans)

def is_right_triangle(x1, y1, x2, y2):
	a = x1**2 + y1**2 # Pythagorean theorem check
	b = x2**2 + y2**2
	c = (x2 - x1)**2 + (y2 - y1)**2
	return (a + b == c) or (b + c == a) or (c + a == b)

if __name__ == "__main__":
	print(compute())