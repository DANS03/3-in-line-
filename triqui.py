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


def print_board(board):
    print("-" * 5)
    for row in board:
        print("|".join(row))
        print("-" * 5)




# ==========================================>GAMERULES


def check_row(row):
    total = 0
    for column in range(3):
        if board[row][column] == "X":
            total += 3
        elif board[row][column] == "O":
            total += 2
            
    return total

def check_column(column):
    total = 0
    for row in range(3):
        if board[row][column] == "X":
            total += 3
        elif board[row][column] == "O":
            total += 2
            
    return total
    
def check_diagonal():
    total = 0
    for diagonal in range(3):
        if board[diagonal][diagonal] == "X":
            total += 3
        elif board[diagonal][diagonal] == "O":
            total += 2
    return total

def check_reversed_diagonal():
    total = 0
    for reversedDiag in range(3):

        if board[2 - reversedDiag][reversedDiag] == "X":
            total += 3
            print(2 - reversedDiag, reversedDiag)
        elif board[2 - reversedDiag][reversedDiag] == "O":
            total += 2
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
            print(2 - reversedDiag, reversedDiag)
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
                values_board[row][column] = str(total)
    
    for diagonal in range(3):
        if int(values_board[diagonal][diagonal]) == -1:
            continue
        else:
            total = check_diagonal()
            if total> int(values_board[diagonal][diagonal]) :
                values_board[diagonal][diagonal] = str(total)
                
            total = check_reversed_diagonal()
            if total> int(values_board[diagonal][diagonal]) :
                values_board[2 - diagonal][diagonal] = str(total)
               
                

# ==========================================>GAMEPLAY


def play():
    keep_playing = True
    playerTurn = True
    playedTurns = 0
    while keep_playing:
        row = int(input("Ingrese la fila: "))
        column = int(input("Ingrese la columna: "))
        valid = validMove(row, column)
        if valid:
            playedTurns += 1
        if valid is True and playerTurn is True:
            board[row][column] = "X"
            values_board[row][column] = "-1"
            playerTurn = turn(playerTurn)

        elif valid is True and playerTurn is False:
            board[row][column] = "O"
            values_board[row][column] = "-1"
            playerTurn = turn(playerTurn)
        else:
            print("Ingrese un movimiento valido.")

        print_board(board)
        heuristic()
        print_board(values_board)

        if playedTurns >= 5:
            print("evaluate winner")
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
