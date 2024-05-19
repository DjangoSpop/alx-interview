#!/usr/bin/python3
"""N Queens placement on NxN chessboard."""

import sys


def generate_solutions(row, column):
    """Solve a simple N x N matrix.

    Args:
        row (int): Number of rows.
        column (int): Number of columns.

    Returns:
        list: A list of lists representing the solutions.
    """
    solution = []
    for queen in range(row):
        solution = place_queen(queen, column, solution)
    return solution


def place_queen(queen, column, prev_solution):
    """Place the queen at a certain position.

    Args:
        queen (int): The row index of the queen.
        column (int): The column to move.
        prev_solution (list): The previous solution.

    Returns:
        list: A list of safe positions for the queen.
    """
    safe_position = []
    for array in prev_solution:
        for x in range(column):
            if is_safe(queen, x, array):
                safe_position.append(array + [x])
    return safe_position


def is_safe(q, x, array):
    """
    Check if it's safe to make a move.

    Args:
        q (int): The row index of the queen.
        x (int): The column index of the queen.
        array (list): The current solution.

    Returns:
        bool: True if the position is safe, False otherwise.
    """
    if x in array:
        return False
    else:
        return all(abs(array[column] - x) != q - column for column in range(q))


def init():
    """Initialize the game.

    Args:
        None

    Returns:
        int: The value of N for the NxN chessboard.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def n_queens():
    """Entry point for the N-Queens problem solver.

    Args:
        None

    Returns:
        None
    """
    n = init()
    solutions = generate_solutions(n, n)
    for array in solutions:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)


if __name__ == '__main__':
    n_queens()
