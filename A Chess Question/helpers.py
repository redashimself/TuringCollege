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


def can_take(white_piece, white_pos, black_pos):
    white_row, white_col = white_pos
    black_row, black_col = black_pos

    if white_piece == "Knight":
        return (abs(white_row - black_row) == 2 and abs(white_col - black_col) == 1) or \
            (abs(white_row - black_row) == 1 and abs(white_col - black_col) == 2)
    elif white_piece == "Rook":
        return white_row == black_row or white_col == black_col

    return False


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
