#==========================================>SPRITES
price = """
             ___________
            '._==_==_=_.'
            .-\\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \\::.    /
               '::. .'
                 ) (
               _.' '._
"""

board = [[" " for _ in range(3)] for _ in range (3)]

def print_board(board):
    print("-" * 5)
    for row in board:
        print("|".join(row))
        print("-" * 5)
#==========================================>GAMERULES       
def win (board):
    
    #3 in line case case
    for column in range(3) :
        sum = 0
        for row in range(3):
            if( board[column][row] == "X"):
                sum += 10
            elif( board[column][row] == "O"):
                sum +=1 
        if( sum == 30): 
            return 'X'
        elif( sum == 3): 
            return 'O'
        
        print(sum)
    
    #3 in line case case
    for column in range(3) :
        sum = 0
        for row in range(3):
            if( board[row][column] == "X"):
                sum += 10
            elif( board[row][column] == "O"):
                sum +=1 
        if( sum == 30): 
            return 'X'
        elif( sum == 3): 
            return 'O'
        
        print(sum)
    #Diagonal case
    sum = 0
    for diagonal in range(3):
        
        if( board[diagonal][diagonal] == 'X'): 
            sum += 10
        elif(board[diagonal][diagonal] == 'O'):
            sum += 1
    if( sum == 30): 
            return 'X'
    elif( sum == 3): 
        return 'O'
    
    #Reversed diagonal  case
    for reversedDiag in range(3):
        
        if( board[2 - reversedDiag][ 2 - reversedDiag] == 'X'): 
            sum += 10
        elif(board[2 - reversedDiag][ 2 - reversedDiag] == 'O'):
            sum += 1
    if( sum == 30): 
            return 'X'
    elif( sum == 3): 
        return 'O'
    
    return None

def turn (value):
    return not value

def validateMove(row, column):
    if (row < 0 or row >= 3):
        return False
    elif (column < 0 or column >= 3):
        return False
    elif(board[row][column] != " "):
        return False
    else:
        return True
    
#==========================================>GAMEPLAY
      
def play(board):
    exit = False
    playerTurn = True 
    playedTurns = 0
    while exit is False:
        row =int(input("Ingrese la fila: "))
        column = int (input("Ingrese la columna: "))
        validate = validateMove(row, column)
        if (validate is True and playerTurn is True):    
            board[row][column] = 'X'
            print_board(board)
            playerTurn = turn(playerTurn)
            print (playerTurn)
        elif(validate is True and playerTurn is False):
            board[row][column] = 'O'
            print_board(board)
            playerTurn = turn(playerTurn)
        else:
            print("Ingrese un movimiento valido.")
        
        playedTurns +=1
        
        if(playedTurns >= 5 ):
            winner = win(board)
            
            if(winner): 
                print(price)
                print("The winner is:"+winner)
                return None
        




        
        
if  __name__ == "__main__":
    play(board)