
# Project Euler problem 67: minimum path sum II

def compute(): #  Loading triangle data from file
    with open("p67.txt", "r") as f:
        lines = f.read().strip().split('\n')
        triangle = [list(map(int, line.split())) for line in lines]

    for i in reversed(range(len(triangle) - 1)): # Iterate backwards from second to last row
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    return str(triangle[0][0]) # Max total path sum is stored in single top element

if __name__ == "__main__":
    print(compute())