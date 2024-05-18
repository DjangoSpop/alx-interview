#!/usr/bin/python3
"""
This module contains a function that solves the N Queens problem.
"""
import sys

def nqueens(n):
    """
    Entry point for the N Queens problem.

    Args:
        n (int or str): The size of the board.

    Prints the solutions to the N Queens problem, if any.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    nqueens(sys.argv[1])

def is_safe(board, row, col, n):
    """
    Checks if a queen can be placed on the board[row][col].

    Args:
        board (list): The current state of the board.
        row (int): The row where the queen is to be placed.
        col (int): The column where the queen is to be placed.
        n (int): The size of the board.

    Returns:
        bool: True if the queen can be placed, False otherwise.
    """
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(n):
    """
    Solves the N Queens problem using backtracking.

    Args:
        n (int): The size of the board.

    Returns:
        list: A list of lists, where each inner list represents
              a solution to the problem.
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def solve(row):
        """
        Recursive helper function to solve the N Queens problem.

        Args:
            row (int): The current row where a queen is to be placed.
        """
        if row == n:
            solution = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = 0

    solve(0)
    return solutions
 