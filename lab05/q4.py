import random


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3)
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")



def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

def return_list_coord(square_num):
    coord = [(square_num - 1)//3, (square_num-1)%3]
    return coord

def put_in_board(board, mark, square_num):
    coord = return_list_coord(square_num)
    board[coord[0]][coord[1]] = mark
    return board

def put_in_board_c(board, mark):
    coord = make_random_move(board, mark)
    board[coord[0]][coord[1]] = mark
    while is_win(board, 'O') == True:
        coord = make_random_move(board, mark)
        board[coord[0]][coord[1]] = mark
    return board

def get_free_squares(board):
    empty_board = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == " ":
                empty_board.append([i, j])
    return empty_board

def make_random_move(board, mark):
    empty_board = get_free_squares(board)
    rand_num = int(len(empty_board) * random.random())
    return empty_board[rand_num]

def is_row_all_marks(board, row_i, mark):
    count = 0
    for i in range(len(board[0])):
        if board[row_i][i] == mark:
            count += 1
    if count == 3:
        return True
    return False

def is_col_all_marks(board, col_i, mark):
    count = 0
    for i in range(len(board)):
        if board[i][col_i] == mark:
            count += 1
    if count == 3:
        return True
    return False

def is_win(board, mark):
    for row_i in range(3):
        if is_row_all_marks(board, row_i, mark) == True:
            return True
    for col_i in range(3):
        if is_col_all_marks(board, col_i, mark) == True:
            return True
    return False

if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)

    print("\n\n")

    end = False
    while end == False:
        choice = input("Play game? (answer y or n) ")
        if choice == 'y':
            count = 0
            square_num = int(input("Input number: "))
            put_in_board(board, 'X', square_num)
            is_win(board, 'X')
            if is_win(board, 'X') == True:
                print("You won!")
                end = True
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == " ":
                        count += 1
            if count-1 == 0:
                print_board_and_legend(board)
                end = True
            put_in_board_c(board, 'O')
            print_board_and_legend(board)
            is_win(board, 'O')
            print("\n\n")
            if is_win(board, 'O') == True:
                print("You lost")
                end = True
        else:
            end = True