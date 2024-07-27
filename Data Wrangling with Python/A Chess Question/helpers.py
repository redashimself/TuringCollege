from column_coordinate import Column


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


def process_piece_placement_input(user_input):
    piece_name, coordinate = user_input.split()
    column_letter, row_number = coordinate[0], int(coordinate[1])
    column = Column[column_letter].value
    row = 8 - row_number
    return row, column, piece_name


def place_piece(chess_board, row, column, piece, color):
    chess_board[row][column]['piece'] = piece
    chess_board[row][column]['color'] = color


def can_take(chess_board, white_piece, white_pos, black_pos):
    if white_piece == "Knight":
        return can_knight_take(white_pos, black_pos)
    elif white_piece == "Rook":
        return can_rook_take(chess_board, white_pos, black_pos)
    return False


def can_knight_take(white_pos, black_pos):
    white_row, white_col = white_pos
    black_row, black_col = black_pos
    row_diff = abs(white_row - black_row)
    col_diff = abs(white_col - black_col)
    return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)


def can_rook_take(chess_board, white_pos, black_pos):
    white_row, white_col = white_pos
    black_row, black_col = black_pos
    if white_row == black_row:
        return is_horizontal_path_clear(chess_board, white_row, white_col, black_col)
    elif white_col == black_col:
        return is_vertical_path_clear(chess_board, white_col, white_row, black_row)
    return False


def is_horizontal_path_clear(chess_board, row, start_col, end_col):
    start, end = min(start_col, end_col), max(start_col, end_col)
    for col in range(start + 1, end):
        if chess_board[row][col]['piece'] is not None:
            return False
    return True


def is_vertical_path_clear(chess_board, col, start_row, end_row):
    start, end = min(start_row, end_row), max(start_row, end_row)
    for row in range(start + 1, end):
        if chess_board[row][col]['piece'] is not None:
            return False
    return True


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
