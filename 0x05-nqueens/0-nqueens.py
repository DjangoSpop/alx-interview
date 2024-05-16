import sys

def is_safe(board, row, col, n):
    # Check if there's a queen in the same column
    """_summary_

    Args:
        board (_type_): _description_
        row (_type_): _description_
        col (_type_): _description_
        n (_type_): _description_

    Returns:
        _type_: _description_
    """    
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens(board, row, n, solutions):
    if row == n:
        # Base case: All queens are placed, solution found
        solutions.append(board[:])  # Append a copy of the board to solutions
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            # Place the queen
            board[row][col] = 1
            
            # Recur to place the next queen
            solve_n_queens(board, row + 1, n, solutions)
            
            # Backtrack
            board[row][col] = 0

def print_solution(solution):
    for row in solution:
        print(' '.join('Q' if cell == 1 else '.' for cell in row))
    print()

def n_queens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    solutions = []
    board = [[0] * n for _ in range(n)]
    solve_n_queens(board, 0, n, solutions)
    
    for solution in solutions:
        print_solution(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    n_queens(n)
