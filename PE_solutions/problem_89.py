
# Project Euler problem 89: roman numerals

ROMAN_NUMERALS_PREFIXES = [
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1),
]

DIGIT_LENGTHS = [0, 1, 2, 3, 2, 1, 2, 3, 4, 2] # Array storing minimal length of Roman numeral for single digit

def parse_roman_numeral(s): # Converts Roman numeral string to integer value
    result = 0
    while len(s) > 0:
        for (prefix, val) in ROMAN_NUMERALS_PREFIXES:
            if s.startswith(prefix):
                result += val
                s = s[len(prefix):]
                break
    return result

def roman_numeral_len(n): # Calc length of minimal Roman numeral for an integer using digit lengths
    result = 0

    if n >= 4000:
        result += 2

    while n > 0:
        result += DIGIT_LENGTHS[n % 10]
        n //= 10
    return result

def compute():
    with open("p89.txt", 'r') as f:
        TO_SIMPLIFY = [line.strip() for line in f if line.strip()]

    ans = sum(len(s) - roman_numeral_len(parse_roman_numeral(s)) for s in TO_SIMPLIFY)
    return str(ans)

if __name__ == "__main__":
    print(compute())
