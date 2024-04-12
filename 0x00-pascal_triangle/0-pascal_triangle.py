import math 

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(math.factorial(i) // (math.factorial(j) * math.factorial(i - j)))
        triangle.append(row)
    return triangle