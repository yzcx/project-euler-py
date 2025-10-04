
# Project Euler problem 81: path sum two ways

def compute():
    with open("p81_82_83.txt", 'r') as f:
        grid = [list(map(int, line.strip().split(','))) for line in f if line.strip()]

    rows = len(grid)
    cols = len(grid[0])

    for i in reversed(range(rows)): # DP, iterate backward from bottom right corner
        for j in reversed(range(cols)):

            if i + 1 < rows and j + 1 < cols: # Check for three possible path states
                grid[i][j] += min(grid[i + 1][j], grid[i][j + 1])
            elif i + 1 < rows:
                grid[i][j] += grid[i + 1][j]
            elif j + 1 < cols:
                grid[i][j] += grid[i][j + 1]
    return str(grid[0][0])

if __name__ == "__main__":
    print(compute())