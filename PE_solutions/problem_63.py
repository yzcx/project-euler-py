
# Project Euler problem 63: powerful digit counts

def compute():
	ans = sum(1
		for i in range(1, 10)
		for j in range(1, 22)
		if len(str(i**j)) == j)
	return str(ans)

if __name__ == "__main__":
	print(compute())