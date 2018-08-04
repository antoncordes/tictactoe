"""
    Tic-Tac-Toe functions
"""

# Congratulations young coder, you know everything you need to know in order to make a game of Tic-Tac-Toe

# Input: board -> 3x3 list
#        rowIndex -> index of row we want to check
#        marker -> string we want to check for in each cell of the row
# Output: return True if all cells are == marker in corresponding row, return False otherwise
def checkRow(board, rowIndex, marker):
    for cell in board[rowIndex]:
        if cell != marker:
            return False
    return True

def checkCol(board, colIndex, marker):
    for row in board:
        if row[colIndex] != marker:
            return False
    return True
    
# Input: board -> 3x3 list of cells
#        marker -> string we want to check in cells
# Output: return True if left diagonal of board contains all marker values
def checkLeftDiag(board, marker):
    for i in range(3):
        if board[i][i] != marker:
            return False
    return True

# Input: board -> 3x3 list of cells
#        marker -> string we want to check in cells
# Output: return True if right diagonal of board contains all marker values
def checkRightDiag(board, marker):
    for i in range(3):
        if board[i][2 - i] != marker:
            return False
    return True

# Input: board -> 3x3 list of cells
#        marker -> string we want to check in cells
# Output: return True if either diagonal of board contains all marker values
def checkDiags(board, marker):
    right = checkRightDiag(board, marker)
    left = checkLeftDiag(board, marker)
    if right == True or left == True:
        return True
    return False

# Input: board -> 3x3 list of cells
#        marker -> string value
# Output: return True if a row on the board contains all marker values. False otherwise
def checkRows(board, marker):
    for i in range(3):
        if checkRow(board, i, marker):
            return True
    return False    
    
def checkCols(board, marker):
    for i in range(3):
        if checkCol(board, i, marker):
            return True
    return False
    
    
# Input: board -> 3x3 list of cells
#        marker -> string value
# Output: return True if there is a three in a row on the board of marker values. False otherwise
def checkWin(board, marker):
    return checkDiags(board, marker) or checkRows(board, marker) or checkCols(board, marker)
    
    
# Input: board -> 3x3 list of cells
# Output: print all cells of the board, each row on a separate line
def printBoard(board):
    for row in board:
        print(row)

# Input: null
# Output: return the row and the column the user selected
def getMove():
    column = int(input("Enter column: "))
    row = int(input("Enter row: "))
    return (row, column)

# Input: row integer, col integer
# Output: return True if user entered valid row and column, False otherwise
def isValidMove(board, row, col):
    return row >= 1 and row <= 3 and col >= 1 and col <= 3 and board[row - 1][col - 1] == " "

# Input: nothing
# Output: return a valid row and colum the user selected
def getValidMove(board):
    x, y = getMove()
    while isValidMove(board, x, y) == False:
        x, y = getMove()
    return (x, y)

# Input: nothing
# Output: nothing
# Description. Play a game of tic tac toe
def playTicTacToe():
    myBoard = [[" ", " ", " "], # 0
               [" ", " ", " "], # 1
               [" ", " ", " "]] # 2
    player1 = "X"
    player2 = "O"
    previousPlayer = player2
    currentPlayer = player1
    while checkWin(myBoard, previousPlayer) == False:
        printBoard(myBoard)
        row, column = getValidMove(myBoard)
        myBoard[row - 1][column - 1] = currentPlayer
        currentPlayer, previousPlayer = (previousPlayer, currentPlayer) # ("X", "O")
    print("winner winner chicken dinner: ", end="")
    print(previousPlayer)

playTicTacToe()