
# Project Euler problem 73: counting fractions in a range

def compute():
	ans = 0
	stack = [(1, 3, 1, 2)]
	while len(stack) > 0: # Loop continues as long as there are subintervals to check
		leftn, leftd, rightn, rightd = stack.pop()
		d = leftd + rightd # Caclulate denom. of the Mediant
		if d <= 12000: # Check if new fraction's denom is within the problem limit
			n = leftn + rightn
			ans += 1
			stack.append((n, d, rightn, rightd))
			stack.append((leftn, leftd, n, d))
	return str(ans)

if __name__ == "__main__":
	print(compute())