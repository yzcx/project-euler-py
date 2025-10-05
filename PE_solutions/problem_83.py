
# Project Euler problem 83: path sum four ways

def compute():
    with open("p81_82_83.txt", 'r') as f:
        GRID = [list(map(int, line.strip().split(','))) for line in f if line.strip()]

    h = len(GRID)
    w = len(GRID[0])
    INFINITY = 1 << 30
    distance = [[INFINITY] * w for _ in range(h)]

    def get_distance(x, y): # Helper function to fetch distances safely
        if x < 0 or x >= w or y < 0 or y >= h:
            return INFINITY
        else:
            return distance[y][x]

    distance[0][0] = GRID[0][0]
    changed = True
    while changed:
        changed = False

        for y in range(h): # Relaxation pass
            for x in range(w):
                temp = GRID[y][x] + min( # Calc min path sum to (y, x) from its four neighbours
                    get_distance(x - 1, y),
                    get_distance(x + 1, y),
                    get_distance(x, y - 1),
                    get_distance(x, y + 1))

                if temp < distance[y][x]: # Relaxation step, if newly calculated path is shorter distance will be updated
                    distance[y][x] = temp
                    changed = True

    return str(distance[h - 1][w - 1])

if __name__ == "__main__":
    print(compute())