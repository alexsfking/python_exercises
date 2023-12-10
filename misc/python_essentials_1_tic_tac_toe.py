from random import randrange 

players_marks_set = set(['X', 'O'])
vaild_move_set = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

def create_board() -> list[str]:
    board = []
    row = []
    for i in range(1,10):
        row.append(str(i))
        if(i % 3 == 0):
            board.append(row)
            row = []
    return board

def display_board(board:list[str]) -> None:
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    top_bottom = '+-------+-------+-------+'
    middle = '|       |       |       |'
    for row in board:
        print(top_bottom)
        print(middle)
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print(middle)
    print(top_bottom)

def enter_move(board:list[str]) -> None:
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    move = None
    while(move == None):
        move = input("Enter your move: ")
        if move not in vaild_move_set:
            move = None
            continue
        for row in board:
            if move in row:
                index = row.index(move)
                if row[index] == move:
                    row[index] = 'O'
                else:
                    move = None
                break
        else:
            move = None


def make_list_of_free_fields(board:list[str]) -> list:
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_row_column_tuple_list = []
    for i, row in enumerate(board):
        for j, box in enumerate(row):
            if(box not in players_marks_set):
                free_row_column_tuple_list.append((i, j))
    return free_row_column_tuple_list



def victory_for(board:list[str], sign:str) -> bool:
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    for row in board:
        row_set = set(row)
        if len(row_set) == 1 and sign in row_set:
            return True
    for i in range(len(board)):
        col = []
        for j in range(len(board)):
            col .append(board[j][i])
        col_set = set(col)
        if len(col_set) == 1 and sign in col_set:
            return True
    diagonal = []
    for i in range(len(board)):
        diagonal.append(board[i][i])
    diagonal_set = set(diagonal)
    if len(diagonal_set) == 1 and sign in diagonal_set:
        return True 
    if board[2][0] == board[1][1] == board[0][2] == sign:
        return True
    return False

def is_draw(board:list[str]) -> bool:
    for row in board:
        for box in row:
            if box in vaild_move_set:
                return False
    return True


def draw_move(board:list[str]):
    # The function draws the computer's move and updates the board.
    free_row_column_tuple_list = make_list_of_free_fields(board)
    tuple_index = randrange(len(free_row_column_tuple_list))
    row, col = free_row_column_tuple_list[tuple_index]
    board[row][col] = 'X'

def initial_computer_move(board:list[str]) -> None:
    board[1][1] = 'X'

board = create_board()
initial_computer_move(board)
while(True):
    display_board(board)
    enter_move(board)
    if victory_for(board, 'O'):
        display_board(board)
        print("You won!")
        break
    if is_draw(board):
        display_board(board)
        print("Draw!")
        break
    draw_move(board)
    if victory_for(board, 'X'):
        display_board(board)
        print("You lost!")
        break
    if is_draw(board):
        display_board(board)
        print("Draw!")
        break