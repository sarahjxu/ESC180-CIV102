"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 28, 2022
"""

def is_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != " ":
                return False
    return True

def is_bounded(board, y_end, x_end, length, d_y, d_x):
    if y_end+d_y > len(board)-1 or y_end+d_y < 0 or x_end+d_x > len(board)-1 or x_end+d_x < 0:
        y_finish = y_end
        x_finish = x_end
    else:
        y_finish = y_end+d_y
        x_finish = x_end+d_x
    if y_end-length*d_y < 0 or x_end-length*d_x < 0 or y_end-length*d_y>len(board)-1 or x_end-length*d_x>len(board)-1:
        y_start = y_end -(length-1)*d_y
        x_start = x_end-(length-1)*d_x
    else:
        y_start = y_end-length*d_y
        x_start = x_end-length*d_x
    start_bound = board[y_start][x_start]
    end_bound = board[y_finish][x_finish]
    if (start_bound != " " or y_end-length*d_y < 0 or x_end-length*d_x < 0) and (end_bound != " " or y_end+d_y >= len(board) or x_end+d_x >= len(board[0])):
        return "CLOSED"
    elif ((start_bound != " " or y_end-length*d_y < 0 or x_end-length*d_x < 0) and end_bound == " ") or (start_bound == " " and (end_bound != " " or y_end+d_y >= len(board) or x_end+d_x >= len(board[0]))):
        return "SEMIOPEN"
    elif (start_bound == " " and end_bound == " "):
        return "OPEN"
    
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    colour = 0
    open_seq_count = 0
    semi_open_seq_count = 0
    y = y_start
    x = x_start
    while y < len(board) and x < len(board) and y >= 0 and x >= 0:
        if board[y][x] == col:
            colour += 1
        if colour == length and is_sequence_complete(board, col, y-d_y*(length - 1), x-d_x*(length-1), length, d_y, d_x):
            res = is_bounded(board, y, x, length, d_y, d_x)
            if res == "OPEN":
                open_seq_count += 1
            elif res == "SEMIOPEN":
                semi_open_seq_count += 1
            colour = 0
        if y+d_y < 8 and x + d_x<8 and y+d_y>-1 and x+d_x>-1:
            if board[y+d_y][x+d_x] != col:
                colour = 0
        y += d_y
        x += d_x
    return open_seq_count, semi_open_seq_count

def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0
    for i in range(len(board)):
        op1, sem1 = detect_row(board, col, 0, i, length, 1, 0)
        open_seq_count += op1
        semi_open_seq_count += sem1
        op2, sem2 = detect_row(board, col, i, 0, length, 0, 1)
        open_seq_count += op2
        semi_open_seq_count += sem2
    for i in range(len(board)-1):
        op3, sem3 = detect_row(board, col, i, 0, length, 1, 1)
        open_seq_count += op3
        semi_open_seq_count += sem3
        op4, sem4 = detect_row(board, col, 0, i+1, length, 1, 1)
        open_seq_count += op4
        semi_open_seq_count += sem4
        op5, sem5 = detect_row(board, col, 0, len(board)-1-i, length, 1, -1)
        open_seq_count += op5
        semi_open_seq_count += sem5
        op6, sem6 = detect_row(board, col, i+1, len(board)-1, length, 1, -1)
        open_seq_count += op6
        semi_open_seq_count += sem6
    return open_seq_count, semi_open_seq_count

def is_sequence_complete(board, col, y_start, x_start, length, d_y, d_x):
    count = 0
    if y_start - d_y >= 0 and x_start - d_x >= 0 and y_start - d_y <len(board) and x_start - d_x <len(board):
        if board[y_start-d_y][x_start-d_x] == col:
            return False
    if y_start + d_y*length < len(board) and x_start + d_x*length < len(board) and y_start + d_y*length > -1 and x_start + d_x*length > -1:
        if board[y_start + d_y*length][x_start + d_x*length] == col:
            return False
    if board[y_start][x_start] == " ":
        return False
    while y_start >= 0 and x_start >= 0 and y_start < len(board) and x_start < len(board):
        if not is_sq_in_board(board, y_start, x_start):
            False
        if board[y_start][x_start] == col:
            count += 1
        if count == length:
            return True
        if y_start+d_y >= 0 and x_start+d_x >= 0 and y_start+d_y < len(board) and x_start+d_x < len(board):
            if board[y_start+d_y][x_start+d_x] != col:
                count = 0
        y_start += d_y
        x_start += d_x
    return False
    
def search_max(board):
    cur_score = 0
    max_score = -100000
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == " ":
                board[y][x] = "b"
                cur_score = score(board)
                max_score = max(cur_score, max_score)
                if max_score == cur_score:
                    move_y = y
                    move_x = x
                board[y][x] = " "
    return move_y, move_x
    
def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    '''b w w w [blank]'''
    open_w = {}
    '''[blank] w w w [blank]'''
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
    '''if it's white's turn and there is open/semi-open, black is doing bad; if black has open sequence and white does not have open sequence of at least 4, black wins'''
    '''if black does not have open sequence of 4, then add...'''
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

def detect_row1(board, col, y_start, x_start, length, d_y, d_x):
    colour = 0
    closed_seq_count = 0
    y = y_start
    x = x_start
    while y < len(board) and x < len(board) and y >= 0 and x >= 0:
        if board[y][x] == col:
            colour += 1
        if colour == length and is_sequence_complete(board, col, y-d_y*(length - 1), x-d_x*(length-1), length, d_y, d_x):
            res = is_bounded(board, y, x, length, d_y, d_x)
            if res == "CLOSED":
                closed_seq_count += 1
            colour = 0
        if y+d_y < 8 and x + d_x<8 and y+d_y>-1 and x+d_x>-1:
            if board[y+d_y][x+d_x] != col:
                colour = 0
        y += d_y
        x += d_x
    return closed_seq_count

def detect_rows1(board, col, length):
    closed_seq_count = 0
    for i in range(len(board)):
        clo1 = detect_row1(board, col, 0, i, length, 1, 0)
        closed_seq_count += clo1
        clo2 = detect_row1(board, col, i, 0, length, 0, 1)
        closed_seq_count += clo2
    for i in range(len(board)-1):
        clo3 = detect_row1(board, col, i, 0, length, 1, 1)
        closed_seq_count += clo3
        clo4 = detect_row1(board, col, 0, i+1, length, 1, 1)
        closed_seq_count += clo4
        clo5 = detect_row1(board, col, 0, len(board)-1-i, length, 1, -1)
        closed_seq_count += clo5
        clo6 = detect_row1(board, col, i+1, len(board)-1, length, 1, -1)
        closed_seq_count += clo6
    return closed_seq_count

def is_win(board):
    count_space = 0
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == " ":
                count_space += 1
            opw, semw = detect_rows(board, "w", 5)
            opb, semb = detect_rows(board, "b", 5)
            clow = detect_rows1(board, "w", 5)
            clob = detect_rows1(board, "b", 5)
            if opw > 0 or semw > 0 or clow > 0:
                return "White won"
            if opb > 0 or semb > 0 or clob > 0:
                return "Black won"
    if count_space == 0:
        return "Draw"
    return "Continue playing"

def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board

def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i)
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
    
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res

def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x

def is_sq_in_board(board, y, x):
    if y < len(board) and x <len(board[0]) and x >=0 and y >= 0:
        return True
    return False

def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0

if __name__ == '__main__':
    print(play_gomoku(8))