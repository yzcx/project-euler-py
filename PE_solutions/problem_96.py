
# Project Euler problem 96: sudoku

def load_puzzles(filename):
    with open(filename, 'r') as f:
        all_lines = [line.strip() for line in f.readlines() if not line.startswith("Grid")]
        return ["".join(all_lines[i:i + 9]) for i in range(0, len(all_lines), 9)]

def solve(puzzlestr):
    assert len(puzzlestr) == 81
    state = [int(c) for c in puzzlestr]

    colfree = [set(range(1, 10)) for _ in range(9)]
    rowfree = [set(range(1, 10)) for _ in range(9)]
    boxfree = [set(range(1, 10)) for _ in range(9)]

    for y in range(9): # Populate constraint sets based on initial digits
        for x in range(9):
            d = state[y * 9 + x]
            if d != 0:
                colfree[x].remove(d)
                rowfree[y].remove(d)
                boxfree[y // 3 * 3 + x // 3].remove(d)

    def recurse(i): # Recursive backtracking helper
        if i == 81:
            return True
        elif state[i] != 0:
            return recurse(i + 1)
        else:
            x = i % 9
            y = i // 9
            j = y // 3 * 3 + x // 3

            candidates = colfree[x].intersection(rowfree[y], boxfree[j])

            for d in candidates:
                state[i] = d
                colfree[x].remove(d)
                rowfree[y].remove(d)
                boxfree[j].remove(d)

                if recurse(i + 1):
                    return True

                colfree[x].add(d) # Backtrack: restore constraints and reset cell
                rowfree[y].add(d)
                boxfree[j].add(d)

            state[i] = 0
            return False

    if not recurse(0):
        return None
    return state

def compute():
    def extract(sudoku):
        return int("".join(map(str, sudoku[: 3])))

    PUZZLES = load_puzzles("p96.txt")

    ans = sum(extract(solve(puz)) for puz in PUZZLES if solve(puz) is not None)
    return str(ans)

if __name__ == "__main__":
    print(compute())