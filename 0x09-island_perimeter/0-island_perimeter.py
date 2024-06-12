#!/usr/bin/python3
# Description: Function that returns the perimeter of the island described in grid
def island_perimeter(grid):
    """_summary_

    Args:
        grid (_type_): _description_

    Returns:
        _type_: _description_
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