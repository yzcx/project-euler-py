
# Project Euler problem 102: triangle containment

def load_triangles(filename):
    with open(filename, 'r') as f:
        lines = [line.strip().split(',') for line in f if line.strip()]
        return [tuple(map(int, coords)) for coords in lines]

def sign(x):
    if x > 0: # Helper function to return sign of number
        return 1
    elif x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        raise ValueError(str(x))

def is_origin_in_triangle(x0, y0, x1, y1, x2, y2):
    s1 = sign(x0 * y1 - y0 * x1) # Calculate signs of cross product
    s2 = sign(x1 * y2 - y1 * x2)
    s3 = sign(x2 * y0 - y2 * x0)
    return 0 in (s1, s2, s3) or s1 == s2 == s3

def compute():
    TRIANGLES = load_triangles("p102.txt")
    ans = sum(1 for coords in TRIANGLES if is_origin_in_triangle(*coords))
    return str(ans)

if __name__ == "__main__":
    print(compute())