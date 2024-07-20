# Define a 2d chess board

# Add all the coordinates 1a, e5 etc...
# Define each chess piece and the move it can make
# Allow addition of white pieces and place them on the board
# Allow addition of black pieces and place them on the board

from enum import Enum

from column_coordinate import Column


def map_letter_to_board_column_coordinate(user_input):
    user_input_split = user_input.split(" ")
    column_letter = user_input_split[1][0]
    column = Column[column_letter].value

    return column


def create_chess_board():
    board = []
    for row in range(8):
        board_row = []
        for column in range(8):
            cell = {
                "piece": None,
                "color": None,
                "position": f"{Column(column).name}{8 - row}"
            }
            board_row.append(cell)
            board.append(board_row)
        return board


def create_piece_properties():
    # Create pieces for white, black, where they can move and their current board position (empty if not selected/not
    # on board)
    pass


def split_user_input(user_input):
    return user_input.split(" ")


def map_number_to_board_row_coordinate(user_input):
    board_row = int(split_user_input(user_input)[1][1])
    actual_row = abs(board_row - 8)

    return actual_row


def get_piece_array_indices(user_input):
    piece, coordinate = user_input.split()
    column_letter, row_number = coordinate[0], int(coordinate[1])

    column = Column[column_letter].value
    row = abs(row_number - 8)

    return row, column, piece


def main():
    chess_board = create_chess_board()
    pieces = create_piece_properties()

    piece_array_indices = get_piece_array_indices()


if __name__ == "__main__":
    main()
