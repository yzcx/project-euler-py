
# Project Euler problem 68: magic 5-gon ring

import itertools

def compute():
    max_s = None

    for state in itertools.permutations(range(1, 11)): # Iterate over all 10 permutations of number 1 through 10
        if state[0] + state[5] + state[6] == \
                state[1] + state[6] + state[7] == \
                state[2] + state[7] + state[8] == \
                state[3] + state[8] + state[9] == \
                state[4] + state[9] + state[5]:

            min_outer_index = 0 # Find the index of lowest external node to create unique solution string
            min_outer = state[0]
            for i in range(1, 5):
                if state[i] < min_outer:
                    min_outer_index = i
                    min_outer = state[i]

            s = "" # Constructing solution string by concatenating triplets clockwise
            for i in range(5):
                outer_idx = (min_outer_index + i) % 5
                inner_idx_1 = outer_idx + 5
                inner_idx_2 = (outer_idx + 1) % 5 + 5

                s += str(state[outer_idx])
                s += str(state[inner_idx_1])
                s += str(state[inner_idx_2])

            if len(s) == 16:
                if max_s is None or s > max_s:
                    max_s = s
    return max_s

if __name__ == "__main__":
    print(compute())