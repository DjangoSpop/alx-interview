#!/usr/bin/python3
# Description: Function that returns the perimeter of the island described in grid
def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid.

    Args:
        grid (List[List[int]]): A rectangular grid of 0s (water) and 1s (land).

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Land cell
                perimeter += 4  # Initialize perimeter with 4 (assuming no neighbors)

                # Check and subtract shared edges with neighbors
                if i > 0 and grid[i - 1][j] == 1:  # Top neighbor
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:  # Left neighbor
                    perimeter -= 2
                if i < rows - 1 and grid[i + 1][j] == 1:  # Bottom neighbor
                    perimeter -= 2
                if j < cols - 1 and grid[i][j + 1] == 1:  # Right neighbor
                    perimeter -= 2

    return perimeter
