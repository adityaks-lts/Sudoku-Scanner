def is_valid_sudoku(board):
    # Check rows
    for i in range(9):
        row_nums = set()
        for j in range(9):
            if board[i][j] != '.':
                if board[i][j] in row_nums:
                    return False
                row_nums.add(board[i][j])
    
    # Check columns
    for j in range(9):
        col_nums = set()
        for i in range(9):
            if board[i][j] != '.':
                if board[i][j] in col_nums:
                    return False
                col_nums.add(board[i][j])
    
    # Check subgrids
    for block in range(9):
        subgrid_nums = []
        start_row = (block // 3) * 3
        start_col = (block % 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] != '.':
                    if board[i][j] in subgrid_nums:
                        return False
                    subgrid_nums.append(board[i][j])
    
    return True


# Example Sudoku board
sudoku_board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '5', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]

if is_valid_sudoku(sudoku_board):
    print("The Sudoku board is valid.")
else:
    print("The Sudoku board is invalid.")
