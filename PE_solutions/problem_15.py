
# Project Euler problem 15

def lattice_path_dp(n: int = 2) -> int:
    matrix = [[0] * (n + 1) for _ in range(n + 1)] # Creating grid to store number of paths to each spot

    for i in range(n + 1): # Filling grid by looping through rows and columns
        for j in range(n + 1):
            if i == 0 or j == 0: # First row and column only has one way to get to each spot
                matrix[i][j] = 1
            else: # Number of paths is the sum of the paths for other spots
                matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j]
    return matrix[n][n]

if __name__ == "__main__":
    print(lattice_path_dp(n=20))