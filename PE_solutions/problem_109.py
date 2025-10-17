
# Project Euler problem 109: darts

def compute():
    points = [i * j for i in range(1, 21) for j in range(1, 4)] + [25, 50] # List of single dart scores
    doublepoints = [i * 2 for i in range(1, 21)] + [25 * 2] # List of required finishing throws (doubles)

    ways = [[[None] * len(points) for j in range(101)] for i in range(3)] # DP table

    def calc_ways(throws, total, maxindex): # Recursive helper function using memoisation (DP)
        if ways[throws][total][maxindex] is None:
            if throws == 0:
                result = 1 if total == 0 else 0
            else:
                result = 0
                if maxindex > 0: # Case A, ways not using max score allowed
                    result += calc_ways(throws, total, maxindex - 1)
                if points[maxindex] <= total: # Case B ways using max score allowed
                    result += calc_ways(throws - 1, total - points[maxindex], maxindex)
            ways[throws][total][maxindex] = result
        return ways[throws][total][maxindex]

    checkouts = 0 # Main logic
    for remainingpoints in range(1, 100): # Iterate through all possible final scores
        for throws in range(3):
            for p in doublepoints:
                if p <= remainingpoints:
                    checkouts += calc_ways(throws, remainingpoints - p, len(points) - 1)
    return str(checkouts)

if __name__ == "__main__":
    print(compute())