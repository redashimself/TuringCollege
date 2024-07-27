from column_coordinate import Column
from helpers import (
    create_chess_board,
    place_piece,
    get_white_piece,
    get_black_pieces,
    can_take
)


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
        if can_take(chess_board, white_piece, (white_row, white_col), (row, col)):
            can_be_taken.append(f"{piece} at {Column(col).name}{8 - row}")

    if can_be_taken:
        print("The white piece can take the following black pieces:")
        for piece in can_be_taken:
            print(piece)
    else:
        print("The white piece cannot take any black pieces.")


if __name__ == "__main__":
    main()

# We assume the input from the user is valid, in terms of piece names,
# coordinates and not putting the piece out of bounds/in the same place. Therefore, we do not validate for this.
# Also, we assume the user is on the white side and our coordinate logic accounts for this
