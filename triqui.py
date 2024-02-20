# ==========================================>SPRITES
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
draw = """
 .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |
| |  ________    | || |  _______     | || |      __      | || | _____  _____ | |
| | |_   ___ `.  | || | |_   __ \\    | || |     /  \\     | || ||_   _||_   _|| |
| |   | |   `. \\ | || |   | |__) |   | || |    / /\\ \\    | || |  | | /\\ | |  | |
| |   | |    | | | || |   |  __ /    | || |   / ____ \\   | || |  | |/  \\| |  | |
| |  _| |___.' / | || |  _| |  \\ \\_  | || | _/ /    \\ \\_ | || |  |   /\\   |  | |
| | |________.'  | || | |____| |___| | || ||____|  |____|| || |  |__/  \\__|  | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------' 
"""

board = [[" " for _ in range(3)] for _ in range(3)]
values_board = [["0" for _ in range(3)] for _ in range(3)]


def print_board(board, name):
    print("-" * 5)
    for row in board:
        print("|".join(row))
        print("-" * 5)

    print("==========================================>"+name)



# ==========================================>GAMERULES


def check_row(row):
    total = 0
    for column in range(3):
        if board[row][column] == "X":
            total += 5
        elif board[row][column] == "O":
            total += 4
        elif board[row][column] == " ":  
            total += 1
    return total

def check_column(column):
    total = 0
    for row in range(3):
        if board[row][column] == "X":
            total += 5
        elif board[row][column] == "O":
            total += 4
        elif board[row][column] == " ":  
            total += 1
            
    return total
    
def check_diagonal():
    total = 0
    for diagonal in range(3):
        if board[diagonal][diagonal] == "X":
            total += 5
        elif board[diagonal][diagonal] == "O":
            total += 4
        elif board[diagonal][diagonal] == " ":  
            total += 1
    return total

def check_reversed_diagonal():
    total = 0
    for reversedDiag in range(3):

        if board[2 - reversedDiag][reversedDiag] == "X":
            total += 5
        elif board[2 - reversedDiag][reversedDiag] == "O":
            total += 4
        elif board[2 - reversedDiag][reversedDiag]  == " ":
            total += 1
    return total

def win():

    # 3 in line case case
    for column in range(3):
        total = 0
        for row in range(3):
            if board[column][row] == "X":
                total += 10
            elif board[column][row] == "O":
                total += 1
        if total == 30:
            return "X"
        elif total == 3:
            return "O"

    # 3 in line case case
    for column in range(3):
        total = 0
        for row in range(3):
            if board[row][column] == "X":
                total += 10
            elif board[row][column] == "O":
                total += 1
        if total == 30:
            return "X"
        elif total == 3:
            return "O"

    # Diagonal case
    total = 0
    for diagonal in range(3):

        if board[diagonal][diagonal] == "X":
            total += 10
        elif board[diagonal][diagonal] == "O":
            total += 1
    if total == 30:
        return "X"
    elif total == 3:
        return "O"

    # Reversed diagonal  case
    total = 0
    for reversedDiag in range(3):

        if board[2 - reversedDiag][reversedDiag] == "X":
            total += 10
            
        elif board[2 - reversedDiag][reversedDiag] == "O":
            total += 1
    if total == 30:
        return "X"
    elif total == 3:
        return "O"

    return None


def turn(value):
    return not value


def validMove(row, column):
    if row < 0 or row >= 3:
        return False
    elif column < 0 or column >= 3:
        return False
    elif board[row][column] != " ":
        return False
    else:
        return True


# ==========================================>Min-Max
def heuristic():
    
    for row in range(3):
        for column in range(3):
            total= 0
            if int(values_board[row][column]) == -1:
               continue 
            else:
                total+= check_row(row) 
                total+= check_column(column)                
                values_board[row][column] = str(total )
    
    for diagonal in range(3):
        if int(values_board[diagonal][diagonal]) == -1:
            continue
        else:
            total = check_diagonal()
            values_board[diagonal][diagonal] =str( int(values_board[diagonal][diagonal] ) + total)
                
            total = check_reversed_diagonal()
            values_board[diagonal][diagonal] =str( int(values_board[2-diagonal][diagonal] ) + total)
            
               
                
def best_move():
    best_position = [0,0]
    highest_value = 0
    for row in range(3):
        for column in range(3):
            if int(values_board[row][column]) >= highest_value:
                best_position[0]= row
                best_position[1]= column
                highest_value=int(values_board[row][column])
                
    return best_position         
# ==========================================>GAMEPLAY


def play():
    keep_playing = True
    playerTurn = True
    playedTurns = 0
    while keep_playing:
        
        if playerTurn is True:
            row = int(input("Ingrese la fila: "))
            column = int(input("Ingrese la columna: "))
            valid = validMove(row, column)
            if valid:
                playedTurns += 1
                board[row][column] = "X"
                values_board[row][column] = "-1"
                playerTurn = turn(playerTurn)
            else:
                print("Ingrese un movimiento valido.")
                continue


        elif  playerTurn is False:
            playedTurns += 1
            row, column = best_move()
            board[row][column] = "O"
            values_board[row][column] = "-1"
            playerTurn = turn(playerTurn)
            
        
        print_board(board,"Game")
        heuristic()
        print_board(values_board,"Heuristic")

        if playedTurns >= 5:
            winner = win()

            if winner:
                print(price)
                print("The winner is:" + winner)
                return None

        if playedTurns > 9:
            print(draw)
            print("Draw!!!")
            return None


if __name__ == "__main__":
    play()
