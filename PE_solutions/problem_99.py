
# Project Euler problem 99: largest exponential

import math

def compute():
    with open("p99.txt", 'r') as f:
        pairs = [line.strip().split(',') for line in f if line.strip()]

    max_log_value = 0.0
    max_line_number = 0

    for line_num, pair in enumerate(pairs, 1): # Iterate through all pairs using enumerate for 1 based line counting
        base = int(pair[0])
        exponent = int(pair[1])

        log_value = exponent * math.log(base) # Calculate log(B^E) = E * log(B)

        if log_value > max_log_value: # Track max value and its line number
            max_log_value = log_value
            max_line_number = line_num
    return str(max_line_number)

if __name__ == "__main__":
    print(compute())