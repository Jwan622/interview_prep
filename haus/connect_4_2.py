import random


def initialize_board():
    """
    Return list of lists, for example:
        # create board
        board = initialize_board()

        # to address a particular position:
        cell = board[row_index][column_index]
    """
    return [[' ' for _ in range(7)] for _ in range(6)]


def print_board(board):
    print("\n".join(str(row_index) + " | " + " | ".join(row) + " |" for row_index, row in enumerate(board))) # a generator inside str function
    print("- " * 16)
    print("    0   1   2   3   4   5   6\n")


def main():
    # example code:  feel free to change
    board = initialize_board()
    print_board(board)
    # let's try to get the drop chip function working asap and test
    move_number = 0
    while True:
        column_to_drop = int(input())
        player_mark = 'X' if move_number % 2 == 0 else 'O'
        print('player mark: ', player_mark)
        row_played = drop_chip(board, column_to_drop, player_mark)
        move_number += 1
        if row_played:
            print_board(board)
            if check_win(board, column_to_drop, row_played, player_mark):
                print('game over')
                break
        else:
            print('illegal move was made')
            break

def check_win(board, column_played, row_played, player_mark):
    # check horizontal first
    print('column played: ', column_played)
    print('row played: ', row_played)
    columns_to_check_left = 1
    column_to_begin_checking_to_left_of = column_played
    while board[row_played][column_played - columns_to_check_left] == player_mark and column_played - columns_to_check_left >= 0:
        column_to_begin_checking_to_left_of = column_played - columns_to_check_left
        columns_to_check_left += 1
    print('column_to_begin_checking_to_left_of:', column_to_begin_checking_to_left_of)
    if all(board[row_played][column_to_begin_checking_to_left_of + i] == player_mark for i in range(1, 4)):
        print(f'{player_mark} has won horizontally')
        return True

    # check vertically next
    print('column played: ', column_played)
    print('row played: ', row_played)
    row_to_check_upwards = 1
    row_to_begin_checking_to_down_from = row_played
    while board[row_played - row_to_check_upwards][column_played] == player_mark and row_played - row_to_check_upwards >= 0:
        row_to_begin_checking_to_down_from = row_played - row_to_check_upwards
        row_to_check_upwards += 1
    print('row to begin_checking_to_down_from:', row_to_begin_checking_to_down_from)
    if row_to_begin_checking_to_down_from <= 2:
        if all(board[row_played + i][column_played] == player_mark for i in range(1, 4)):
            print(f'{player_mark} has won vertically')
            return True

    # check diagonally next. we want to check up right from most lower left corner
    row_to_check_down_diag_to = 1
    column_to_check_left_diag_to = 1
    row_to_begin_checking_diag_up_from = row_played
    column_to_begin_checking_diag_up_from = column_played
    while row_played + row_to_check_down_diag_to <= 5 and board[row_played + row_to_check_down_diag_to][column_played - column_to_check_left_diag_to] == player_mark and column_played - column_to_check_left_diag_to >= 0:
        row_to_begin_checking_diag_up_from = row_played + row_to_check_down_diag_to
        column_to_begin_checking_diag_up_from = column_played - column_to_check_left_diag_to
        row_to_check_down_diag_to += 1
        column_to_check_left_diag_to += 1
    print('row to begin checking diag up from:', row_to_begin_checking_diag_up_from)
    print('column to begin checking diag up from:', column_to_begin_checking_diag_up_from)
    if all(board[row_to_begin_checking_diag_up_from - i][column_to_begin_checking_diag_up_from + i] == player_mark for i in range(1,4)):
        print('f{player_mark} has won diagonally')
        return True
    return False


def drop_chip(board, column_to_drop, player_mark):
    for row_index in range(len(board) - 1, -1, -1):
        if board[row_index][column_to_drop] == ' ':
            board[row_index][column_to_drop] = player_mark
            return row_index
    return None
if __name__ == "__main__":
    main()






