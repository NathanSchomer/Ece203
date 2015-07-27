#2 player, tic tac toe

def checkForWin(board):
    #check for horizontal win
    if(board[0] != '-' and board[0] == board[1] and board[1] == board[2]):
        return board[0]
    if(board[3] != '-' and board[3] == board[4] and board[4] == board[5]):
        return board[3]
    if(board[6] != '-' and board[6] == board[7] and board[7] == board[8]):
        return board[6]
    
    #check for vertical win
    if(board[0] != '-' and board[0] == board[3] and board[3] == board[6]):
        return board[0]
    if(board[1] != '-' and board[1] == board[4] and board[4] == board[7]):
        return board[1]
    if(board[2] != '-' and board[2] == board[5] and board[5] == board[8]):
        return board[2]

    #check for diagonal win
    if(board[0] != '-' and board[0] == board[4] and board[4] == board[8]):
        return board[0]
    if(board[2] != '-' and board[2] == board[4] and board[4] == board[6]):
        return board[2]

    return 0

def setMark(board, x, y, val):
    if( x <= 3 and y <= 3 and board[(x-1) + (y-1)*3] == '-'):
        board[(x-1) + (y-1)*3] = val
        return 0;
    else:
        return -1;

def player1move(board):
    print('Player 1 Place Mark:')
    y = int(raw_input('row '))
    x = int(raw_input('col '))
    setMark(board, x, y, 'X')
    return board

def player2move(board):
    print('\nPlayer 2 Place Mark')
    y = int(raw_input('row '))
    x = int(raw_input('col '))
    setMark(board, x, y, 'O')
    return board

def printBoard(board):
    print '\n%s\t%s\t%s\n\n\n%s\t%s\t%s\n\n\n%s\t%s\t%s\n' %(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8])
    return 0

board = ['-','-','-','-','-','-','-','-','-']

while(checkForWin(board) == 0):
    printBoard(board)
    player1move(board)
    if(checkForWin(board) != 0): 
        break
    printBoard(board)
    player2move(board)

print '\nWIN: %s' %checkForWin(board)
