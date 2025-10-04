
# Project Euler problem 82: path sum three ways

def load_grid(filename):
    with open(filename, 'r') as f:
        return [list(map(int, line.strip().split(','))) for line in f if line.strip()]

def compute():
    GRID = load_grid("p81_82_83.txt")

    h = len(GRID)
    w = len(GRID[0])

    INFINITY = float('inf')

    def get_distance(x, y): # Helper function to fetch distances from DP table safely. Treating boundaries as infinity
        if x < 0 or y < 0 or y >= h or x >= w:
            return INFINITY
        else:
            return distance[y][x]

    distance = [[0] * w for _ in range(h)]

    for y in range(h):
        distance[y][0] = GRID[y][0]

    for x in range(1, w): # DP, iterate column by column L to R
        for y in range(h):
            distance[y][x] = GRID[y][x] + min(get_distance(x - 1, y), get_distance(x, y - 1))

        for y in reversed(range(h)):
            distance[y][x] = min(distance[y][x], GRID[y][x] + get_distance(x, y + 1))

    ans = min(distance[y][w - 1] for y in range(h))
    return str(ans)

if __name__ == "__main__":
    print(compute())