import random
import time

BOARD_WIDTH = 9
BOARD_HEIGHT = 9


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


def find_all_possible_solutions(board, count=0):
    for row_index, row in enumerate(board):
        for col_index, cell in enumerate(row):
            if cell == "":
                print(f"FOUND EMPTY CELL: {row_index} {col_index}")
                for number in range(1, 9):
                    board[row_index][col_index] = str(number)

                    # Check if the newly added number is valid there
                    if is_valid(board):
                        # Check if it is now a full board
                        if not any("" in r for r in board):
                            count += 1

                        if find_all_possible_solutions(board, count):
                            return True

                    # Revert it
                    board[row_index][col_index] = ""

                return False

    print(count)
    return True



if __name__ == '__main__':
    b = [['3', '1', '6', '', '', '5', '7', '2', '4'], ['2', '5', '7', '4', '3', '6', '1', '8', '9'], ['9', '8', '4', '1', '2', '7', '6', '5', '3'], ['7', '6', '8', '3', '5', '2', '4', '9', '1'], ['1', '2', '9', '7', '4', '8', '3', '6', '5'], ['4', '3', '5', '6', '1', '9', '2', '7', '8'], ['6', '9', '1', '5', '7', '4', '8', '3', '2'], ['8', '4', '2', '9', '6', '3', '5', '1', '7'], ['5', '7', '3', '2', '8', '1', '9', '4', '6']]

    find_all_possible_solutions(b)

    # display_board(generate_board())
