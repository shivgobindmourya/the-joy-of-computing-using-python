import numpy

board = numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])

pl1 = 'X'
pl2 = 'O'


def check_rows(symbol):
    for r in range(3):
        count = 0
        for c in range(3):
            if board[r][c] == symbol:
                count=count+1
        if count == 3:
            print(symbol, 'won')
            return True
    return False

def check_cols(symbol):
    for c in range(3):
        count = 0
        for r in range(3):
            if board[r][c] == symbol:
                count=count+1
        if count == 3:
            print(symbol, 'won')
            return True
    return False


def check_diagonals(symbol):
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        print(symbol, 'won')
        return True
    if board[2][0] == board[1][1] == board[0][2] == symbol:
        print(symbol, 'won')
        return True
    return False

def display_board():
    print("\nCurrent Board: ")
    for row in board:
        print(" | ".join(row))   # 🔥 changed (better UI)
        print("-" * 9)

def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol)

def place(symbol):
    display_board() 
    
    while True:
        row=int(input('Enter your row (1 or 2 or 3) : '))
        col=int(input('Enter your col (1 or 2 or 3) : '))
        if row>0 and row<4 and col>0 and col<4 and (board[row-1][col-1]== "-"):
            break
        else:
            print("Invalid Input. Please enter again")
    board[row-1][col-1] = symbol


def play():
    for turn in range(9):
        if turn%2 ==0:
            print('\n ----X turn----')
            place(pl1)
            if won(pl1):
                display_board()   # show final board
                break
        else:
            print('\n ----O turn----')
            place(pl2)
            if won(pl2):
                display_board()
                break
    if not(won(pl1)) and not(won(pl2)):
            display_board()
            print("Draw")


play()