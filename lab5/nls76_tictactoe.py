#2 player, tic tac toe

def checkForWin(board):
    #check for horizontal win
    if(board[0] == board[1] && board[1] == board[2])
        return board[0]
    if(board[3] == board[4] && board[4] == board[5])
        return board[3]
    if(board[6] == board[7] && board[7] == board[8])
        return board[6]
    
    #check for vertical win
    if(board[0] == board[3] && board[3] == board[6])
        return board[0]
    if(board[1] == board[4] && board[4] == board[7])
        return board[3]
    if(board[2] == board[5] && board[5] == board[8])
        return board[6]

    #check for diagonal win
    if(board[0] == board[1] && board[1] == board[2])
        return board[0]
    if(board[3] == board[4] && board[4] == board[5])
        return board[3]

    sum(board[0:2]) == 3 || sum(board[3:5] >= 3 || sum(board[6:8] >= 0)
            return board 

def setMark():
    return 0

def player1move():
    return 1

def player2move():
    return 2

board = ['-','-','-','-','-','-','-','-','-']

checkForWin(board)
