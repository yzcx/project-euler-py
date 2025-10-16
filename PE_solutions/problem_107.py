
# Project Euler problem 107: minimal network

def load_matrix(filename="p107.txt"):
    with open(filename, 'r') as f:
        raw_lines = [line.strip() for line in f if line.strip()]

    matrix = []
    for line in raw_lines:
        row = [int(val) if val.isdigit() else -1 for val in line.split(',')]
        matrix.append(row)
    return matrix

def compute():
    WEIGHTS = load_matrix("p107.txt")
    numnodes = len(WEIGHTS)

    oldweight = sum(WEIGHTS[i][j] # Add up all undirected ege wedges
                    for i in range(numnodes)
                    for j in range(i + 1, numnodes)  # Only checks the upper triangle undirected edges
                    if WEIGHTS[i][j] != -1)

    connected = set([0])
    newweight = 0

    for _ in range(numnodes - 1):
        lowestweight, newnode = min( # Minimum weight edge that connects node in tree to one outside tree
            (WEIGHTS[j][k], k)
            for j in connected
            for k in range(numnodes)
            if k not in connected and WEIGHTS[j][k] != -1)

        connected.add(newnode)
        newweight += lowestweight

    ans = oldweight - newweight
    return str(ans)

if __name__ == "__main__":
    print(compute())