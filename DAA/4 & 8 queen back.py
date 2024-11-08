def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if i < len(board) and board[i] == j:
            return False
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if i < len(board) and board[i] == j:
            return False

    return True

def solve_n_queens(board, row):

    if row >= len(board):
        return True  

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col 
            if solve_n_queens(board, row + 1):
                return True  
            board[row] = -1  

    return False

def print_board(board):
    n = len(board)
    for i in range(n):
        row = ["Q" if board[i] == j else "." for j in range(n)]
        print(" ".join(row))
    print("\n")
try:
    n = int(input("Enter the size of the board (4 for 4-Queens or 8 for 8-Queens): "))
    if n not in (4, 8):
        print("Please enter 4 or 8 only.")
    else:
        row = int(input(f"Enter the row for the first queen (0-{n-1}): "))
        col = int(input(f"Enter the column for the first queen (0-{n-1}): "))
        board = [-1] * n
        board[row] = col 

        if solve_n_queens(board, row + 1):
            print(f"Solution to the {n}-Queens problem:")
            print_board(board)
        else:
            print("No solution exists with the first queen placed at this position.")

except ValueError:
    print("Please enter valid integer values for board size, row, and column.")

