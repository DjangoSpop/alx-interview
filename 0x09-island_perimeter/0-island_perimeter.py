#!/usr/bin/python3
"""
This module calculates the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    Args:
        grid (List[List[int]]): A 2D grid representing the island.

    Returns:
        int: The perimeter of the island.
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

    return perimeter
