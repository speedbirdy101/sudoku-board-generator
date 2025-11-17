BOARD_WIDTH = 9
BOARD_HEIGHT = 9


def remove_spaces(l):
    res = [i for i in l if i != ""]

    return res


def display_board(board):
    for row in board:
        print(f"| {' | '.join(list(row))} |")


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


def generate_board():
    sudoku_board = [["-" for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
    """
    sudoku_board = [
        ['', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', ''], 
        ['', '', '', '', '', '', '', '', ''], 
        ['', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '']
    ]
    """

    display_board(sudoku_board)

    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):
            cell = sudoku_board[row][col]

    return sudoku_board


if __name__ == '__main__':
    print(generate_board())
