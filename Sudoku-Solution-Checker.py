def checkBoxes(board):
    for row in range(0,9,3):
        for col in range(0,9,3):
            values = board[row][col:col + 3]
            values.extend(board[row+1][col:col + 3])
            values.extend(board[row+2][col:col + 3])
            return len(set(values)) == 9
            
def checkRows(board):
    for i in range(9):
        valid = len(set(board[i])) == 9
        if (valid == False):
            return False
    return True
        
def checkCols(board):
    for i in range(9):
        col = [item[i] for item in board]
        valid = len(set(col)) == 9
        if (valid == False):
            return False
    return True

def valid_solution(board):
    valid = checkBoxes(board) and checkRows(board) and checkCols(board)
    return valid
        