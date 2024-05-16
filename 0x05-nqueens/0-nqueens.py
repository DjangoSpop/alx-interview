"""check_arguments()
initialize_board()
solve_nqueens(board, column=0)

function solve_nqueens(board, column):
    if column == N:
        print_solution(board)
        return

    for row in range(N):
        if is_safe(board, row, column):
            place_queen(board, row, column)
            solve_nqueens(board, column + 1)
            remove_queen(board, row, column)

function is_safe(board, row, column):
    check if there are any queens in the same row, column, or diagonals
    return True if the position is safe, False otherwise

function place_queen(board, row, column):
    mark the position (row, column) as occupied on the board

function remove_queen(board, row, column):
    mark the position (row, column) as unoccupied on the board

function print_solution(board):
    print the solution in the required format"""
import sys 
def check_arguments():
    """Check the number of arguments"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    return N
def initialize_board():
    """Initialize the board"""
    N = check_arguments()
    board = [[0 for i in range(N)] for j in range(N)]
    return board
def is_safe(board, row, column):
    """Check if a queen can be placed on board[row][column]"""
    N = len(board)
    for i in range(column):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False
    return True
def solve_nqueens(board, column = 0):
    """Solve the N queens problem"""
    N = len(board)
    if column == N:
        print_solution(board)
        return
    for row in range(N):
        if is_safe(board, row, column):
            place_queen(board, row, column)
            solve_nqueens(board, column + 1)
            remove_queen(board, row, column)
def place_queen(board, row , column):
    """Place a queen on board[row][column]"""
    board[row][column] = 1
def remove_queen(board, row, column):
    """Remove a queen from board[row][column]"""
    board[row][column] = 0
def print_solution(board):
    """Print the solution in the required format"""
    N = len(board)
    result = []
    for row in range(N):
        for column in range(N):
            if board[row][column] == 1:
                result.append([row, column])
    print(result)

    