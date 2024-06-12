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
                # Count edges shared with water cells
                perimeter += sum(grid[i][j] != grid[i][k] for k in (j-1, j+1) if 0 <= k < cols)
                perimeter += sum(grid[i][j] != grid[k][j] for k in (i-1, i+1) if 0 <= k < rows)

    return perimeter
