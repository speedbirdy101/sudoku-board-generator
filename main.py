import random
import time
from copy import deepcopy

BOARD_WIDTH = 9
BOARD_HEIGHT = 9
POSSIBLE_NUMBER_SET = {str(i) for i in range(1, 10)}


def remove_spaces(l):
    res = [i for i in l if i != ""]

    return res


def display_board(board):
    for row in board:
        row = [x if x != "" else "-" for x in row]
        print(f"| {' | '.join(row)} |")


def is_valid(board: list[list]) -> bool:
    # Check each row
    for row in board:
        row_ = remove_spaces(row)
        if len(row_) != len(set(row_)): # There are repeating elements
            return False

    # Check each column
    for col in range(BOARD_WIDTH):
        column = [x[col] for x in board]
        column = remove_spaces(column)
        if len(column) != len(set(column)): # There are repeating elements:
            return False

    # Now we will try each 3x3 box
    box = 3
    for y_box in range(0, BOARD_HEIGHT, 3):
        for x_box in range(0, BOARD_WIDTH, 3):
            # We are now in the top left of the box
            box_elements = []
            for y_inner in range(box):
                for x_inner in range(box):
                    box_elements.append(board[y_box + y_inner][x_box + x_inner])

            # Remove any empty cells
            box_elements = remove_spaces(box_elements)
            if len(box_elements) != len(set(box_elements)):
                return False

    return True

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def backtrack(board):
    for row_index, row in enumerate(board):
        for cell_col_index, column in enumerate(row):
            if column == "":
                random.shuffle(number_list)
                for possible_number in number_list:
                    board[row_index][cell_col_index] = str(possible_number)

                    # display_board(board)

                    if is_valid(board):  # By placing that number there, it does not make the board invalid so we can carry on
                        if backtrack(board)[0]:
                            return True, board

                    # Revert it because by placing a number there, means the next one is invalid
                    board[row_index][cell_col_index] = ""

                return False, board  # No number can be placed here, backtrack it and try again

    return True, board # Every cell is filled


def generate_board():
    sudoku_board = [["" for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

    backtrack_outcome, sudoku_board = backtrack(sudoku_board)

    return sudoku_board


def is_solvable(board):
    while True:
        found_a_cell = False
        found_empty_cell = False

        # Check each row
        for ri, row in enumerate(board):
            set_row = set(row)
            differences = POSSIBLE_NUMBER_SET - set_row

            print("DIFF", differences)
            if len(differences) == 1:  # There is only one possible option it could be, so we know what to fill it in as
                board[ri][row.index("")] = list(differences)[0]
                found_a_cell = True

        # Check each column
        columns = [
            [r[c] for r in board] for c in range(BOARD_WIDTH)
        ]
        for ci, column in enumerate(columns):
            col_set = set(column)
            differences = POSSIBLE_NUMBER_SET - col_set

            if len(differences) == 1:  # There is only one possible option it could be, so we know what to fill it in as
                board[column.index("")][ci] = list(differences)[0]
                found_a_cell = True

        if not found_a_cell:
            print("falso")
            return False


def generate_playable(board, still_playable=True):
    # Pick a random cell to delete
    random_y, random_x = random.randint(0, len(board) - 1), random.randint(0, len(board) - 1)
    print(random_y, random_x)

    # Remove it
    buffer = board[random_y][random_x]
    board[random_y][random_x] = ""

    display_board(board)

    # Check it is still solvable
    boardcopy = deepcopy(board)
    if is_solvable(boardcopy):
        return generate_playable(board, True)

    else:
        # If it is not solvable anymore, we put it back to what it was before and stop removing (return board, False (not playable))
        board[random_y][random_x] = buffer
        return board, False


if __name__ == '__main__':
    generated_board = generate_board()
    display_board(generated_board)

    b, o = generate_playable(generated_board)
    display_board(b)
