"""module to nqueens"""
#!/usr/bin/python3
"""N Queens Solver"""
import sys

def is_safe(board, row, col, n):
    """
    Check if a queen can be placed on board[row][col]
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(n):
    """
    Solve the N-Queens problem using backtracking
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def solve(board, col):
        """
        Recursive helper function to solve the N-Queens problem
        """
        # Base case: If all queens are placed, add the solution to the list
        if col == n:
            solution = []
            for row in range(n):
                for col in range(n):
                    if board[row][col] == 1:
                        solution.append([row, col])
            solutions.append(solution)
            return

        # Place this queen in all rows one by one
        for row in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1

                # Recur to place rest of the queens
                solve(board, col + 1)

                # If placing queen in board[row][col] doesn't lead to a solution,
                # remove the queen
                board[row][col] = 0

    solve(board, 0)
    return solutions

def nqueens(argv):
    """
    Entry point for the N-Queens problem solver
    """
    if len(argv) != 2:
        print("Usage: nqueens N")
        return 1

    try:
        n = int(argv[1])
    except ValueError:
        print("N must be a number")
        return 1

    if n < 4:
        print("N must be at least 4")
        return 1

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)

    return 0

if __name__ == "__main__":
    exit(nqueens(sys.argv))
    