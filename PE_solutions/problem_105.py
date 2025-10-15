
# Project Euler problem 105: special subset sums testing

def load_sets(filename):
    try:
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
            return [list(map(int, line.split(','))) for line in lines]
    except FileNotFoundError:
        return []

def is_special_sum_set(s):
    s.sort() # Sort set first for efficient check
    sumsseen = set() # Set to track unique subset sums found
    minsum = [None] * (len(s) + 1) # Arrays to track min and max sum for each subset size k
    maxsum = [None] * (len(s) + 1)

    def explore_subsets(i, count, sum): # Recursive function to generate 2^n subsets
        if i == len(s):
            sumsseen.add(sum)
            if minsum[count] is None or sum < minsum[count]:
                minsum[count] = sum
            if maxsum[count] is None or sum > maxsum[count]:
                maxsum[count] = sum
        else:
            explore_subsets(i + 1, count, sum) # Recursive choice 1, exclude element
            explore_subsets(i + 1, count + 1, sum + s[i]) # Recursive choice 2, include element
    explore_subsets(0, 0, 0)

    rule1_satisfied = len(sumsseen) == 2 ** len(s)
    rule2_satisfied = all(maxsum[i] < minsum[i + 1] for i in range(len(s)))
    return rule1_satisfied and rule2_satisfied

def compute():
    SETS = load_sets("p105.txt")
    ans = sum(sum(s) for s in SETS if is_special_sum_set(s))
    return str(ans)

if __name__ == "__main__":
    print(compute())