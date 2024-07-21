# Define a 2d chess board [x]
# Add all the coordinates 1a, e5 etc... [x]
# Define each chess piece and the move it can make [x] -> Only need to define Rook and Knight
# Allow addition of pieces and place them on the board [x]

from column_coordinate import Column


def get_white_piece():
    user_input = input("Enter white piece (Knight or Rook) and position (e.g., Knight e4): ").strip()

    return process_piece_placement_input(user_input)


def get_black_pieces():
    black_pieces = []
    while len(black_pieces) < 16:
        user_input = input("Enter black piece and position (e.g., Knight e5) or 'done' to finish: ").strip()
        if user_input.lower() == 'done':
            if len(black_pieces) == 0:
                print("You must add at least one black piece.")
                continue
            break

        row, column, piece_name = process_piece_placement_input(user_input)
        black_pieces.append((row, column, piece_name))
        print(f"{piece_name} added at {Column(column).name}{8 - row}")

    return black_pieces


def can_take(white_piece, white_pos, black_pos):
    white_row, white_col = white_pos
    black_row, black_col = black_pos

    if white_piece == "Knight":
        # 1st, check for 2 squares vertically and 1 horizontally
        # Or, check for 2 squares horizontally and 1 vertically
        return (abs(white_row - black_row) == 2 and abs(white_col - black_col) == 1) or \
            (abs(white_row - black_row) == 1 and abs(white_col - black_col) == 2)
    # Check if the rows are the same (horizontal movement)
    # Check if  columns are the same (vertical movement)
    elif white_piece == "Rook":
        return white_row == black_row or white_col == black_col

    return False


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


def map_number_to_board_row_coordinate(user_input):
    board_row = int(user_input.split()[1][1])
    actual_row = abs(board_row - 8)

    return actual_row


def process_piece_placement_input(user_input):
    piece_name, coordinate = user_input.split()
    column_letter, row_number = coordinate[0], int(coordinate[1])

    column = Column[column_letter].value
    row = 8 - row_number

    return row, column, piece_name


def place_piece(chess_board, row, column, piece, color):
    chess_board[row][column]['piece'] = piece
    chess_board[row][column]['color'] = color


def main():
    chess_board = create_chess_board()

    # Get white piece and place it on the board
    white_row, white_col, white_piece = get_white_piece()
    place_piece(chess_board, white_row, white_col, white_piece, "White")
    print(f"White {white_piece} placed at {Column(white_col).name}{8 - white_row}")

    # Get black pieces and place them on the board
    black_pieces = get_black_pieces()
    for row, col, piece in black_pieces:
        place_piece(chess_board, row, col, piece, "Black")

    # Check which black pieces can be taken
    can_be_taken = []
    for row, col, piece in black_pieces:
        if can_take(white_piece, (white_row, white_col), (row, col)):
            can_be_taken.append(f"{piece} at {Column(col).name}{8 - row}")

    if can_be_taken:
        print("The white piece can take the following black pieces:")
        for piece in can_be_taken:
            print(piece)
    else:
        print("The white piece cannot take any black pieces.")


if __name__ == "__main__":
    main()
