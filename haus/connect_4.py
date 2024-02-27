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
    print("\n".join(str(row_index) + " | " + " | ".join(row) + " |" for row_index, row in enumerate(board)))
    print("- " * 16)
    print("    0   1   2   3   4   5   6\n")


def main():
    # example code:  feel free to change
    board = initialize_board()
    print_board(board)
    move_number = 0
    move_count_total = 4
    while True:  # when game is won
        move = int(input())
        player_mark = 'X' if move_number % 2 == 0 else 'O'  # somehow we need to alternate between player 1 and 2
        print('move: ', move)
        index_placed = drop_disk(move, board, player_mark)
        if check_win_after_move(board, move, index_placed):
            break
        move_number += 1

    print('end of game reahced =======================================')

    # game logic goes here

    # helpful code snippets:
    # generates random int btw 3 and 9, inclusive
    # random.randint(3, 9)
    # while game is not won
    # players to alterate choooising a column to drop into
    # what shold teh choice do? say player says 3
    # player 1 is X, player 2 is O
    # what's the best way to drop a disk? wherever we drop teh risk, place an X or O


def drop_disk(column, board, mark_to_make):
    index_to_return = 0
    for index in range(len(board) - 1, -1, -1):  # we iterate through rorws first and each row has a column
        if board[index][column] == ' ':
            board[index][column] = mark_to_make
            index_to_return = index
            break
    print_board(board)
    return index_to_return


def check_win_after_move(board, column_to_check, row_to_check):
    player_mark = board[row_to_check][column_to_check]
    print('row to check:', row_to_check)
    print('coilumn to check:', column_to_check)
    starting_column_boundary_on_left = None
    how_many_left = 1
    while starting_column_boundary_on_left is None:
        print('in while loop for win checking')
        if board[row_to_check][column_to_check - how_many_left] == player_mark:
            how_many_left += 1
        else:
            starting_column_boundary_on_left = column_to_check - how_many_left + 1

    print('found starting_column_boundary_on_left: ', starting_column_boundary_on_left)

    # now we check if all columns 3 to right are the same as player_mark
    if all(board[row_to_check][starting_column_boundary_on_left + i] == player_mark for i in range(1, 4)):
        print('x has won')
        return True

    return False


if __name__ == "__main__":
    main()





