#!/usr/bin/python3
""" N queens puzzle, challenge of placing N non-attacking queens
on a NxN chessboard
This program solves the N queens problem """

""" N queens puzzle, challenge of placing N non-attacking queens
on a NxN chessboard
This program solves the N queens problem """

from sys import argv, exit


def is_NQueen(cell: list) -> bool:
    """Check if the queen in the given cell is safe."""
    row_number = len(cell) - 1
    for index in range(row_number):
        difference = abs(cell[index] - cell[row_number])
        if difference == 0 or difference == row_number - index:
            return False
    return True


def solve_NQueens(dimension: int, row: int, cell: list, output: list):
    """Solve the N queens problem recursively."""
    if row == dimension:
        print(output)
    else:
        for column in range(dimension):
            cell.append(column)
            if is_NQueen(cell):
                output.append([row, column])
                solve_NQueens(dimension, row + 1, cell, output)
                output.pop()
            cell.pop()


if __name__ == "__main__":
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        N = int(argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)
    if N < 4:
        print('N must be at least 4')
        exit(1)
    else:
        output = []
        cell = 0
        solve_NQueens(N, 0, [], output)
