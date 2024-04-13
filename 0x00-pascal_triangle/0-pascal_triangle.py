#!/usr/bin/python3
def pascal_triangle(n):
  """
  This function returns a list of lists representing the Pascal's triangle of size n.

  Args:
      n: An integer representing the number of rows in the Pascal's triangle.

  Returns:
      A list of lists containing the Pascal's triangle elements. Returns an empty list 
      if n is less than or equal to 0.
  """

  if n <= 0:
    return []

  # Initialize the first two rows (base cases)
  triangle = [[1]]  # First row is always [1]
  if n >= 2:
    triangle.append([1, 1])  # Second row is always [1, 1]

  # Generate remaining rows using list comprehensions
  for i in range(2, n):
    previous_row = triangle[i-1]
    new_row = [previous_row[j-1] + previous_row[j] for j in range(1, i)]
    new_row.insert(0, 1)  # Add 1 at the beginning of the row
    new_row.append(1)  # Add 1 at the end of the row
    triangle.append(new_row)

  return triangle

# # Example usage
# n = 5
# triangle = pascal_triangle(n)
# print(triangle)  # Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
