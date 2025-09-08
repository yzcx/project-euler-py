
# Project Euler problem 30: digit fifth powers

def compute():
	ans = sum(i for i in range(2, 1000000) if i == fifth_power_digit_sum(i))
	return str(ans)

def fifth_power_digit_sum(n):
	return sum(int(c)**5 for c in str(n))

if __name__ == "__main__":
	print(compute())