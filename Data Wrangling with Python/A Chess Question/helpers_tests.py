from helpers import place_piece, create_chess_board, process_piece_placement_input, can_take


def test_process_piece_placement_input():
    row, col, piece = process_piece_placement_input("Knight e4")
    assert row == 4
    assert col == 4
    assert piece == "Knight"

    # Test bottom left
    row, col, piece = process_piece_placement_input("Rook a1")
    assert row == 7
    assert col == 0
    assert piece == "Rook"

    # Test top right
    row, col, piece = process_piece_placement_input("Queen h8")
    assert row == 0
    assert col == 7
    assert piece == "Queen"


def test_place_piece():
    chess_board = create_chess_board()
    place_piece(chess_board, 3, 4, "Knight", "White")
    assert chess_board[3][4]['piece'] == "Knight"
    assert chess_board[3][4]['color'] == "White"
    assert chess_board[3][4]['position'] == "e5"

    # Check if surrounded pieces unaffected
    assert chess_board[3][3]['piece'] is None
    assert chess_board[3][5]['piece'] is None
    assert chess_board[2][4]['piece'] is None
    assert chess_board[4][4]['piece'] is None


def test_can_take_knight():
    chess_board = create_chess_board()
    assert can_take(chess_board, "Knight", (4, 4), (6, 5))
    assert can_take(chess_board, "Knight", (4, 4), (6, 3))
    assert can_take(chess_board, "Knight", (4, 4), (2, 5))
    assert can_take(chess_board, "Knight", (4, 4), (2, 3))
    assert can_take(chess_board, "Knight", (4, 4), (5, 6))
    assert can_take(chess_board, "Knight", (4, 4), (5, 2))
    assert can_take(chess_board, "Knight", (4, 4), (3, 6))
    assert can_take(chess_board, "Knight", (4, 4), (3, 2))

    assert not can_take(chess_board, "Knight", (4, 4), (4, 5))  # Adjacent square
    assert not can_take(chess_board, "Knight", (4, 4), (6, 6))  # Diagonal move
    assert not can_take(chess_board, "Knight", (4, 4), (7, 7))  # Far away


def test_can_take_rook():
    chess_board = create_chess_board()
    assert can_take(chess_board, "Rook", (4, 4), (4, 7))  # Same row
    assert can_take(chess_board, "Rook", (4, 4), (4, 0))  # Same row
    assert can_take(chess_board, "Rook", (4, 4), (7, 4))  # Same column
    assert can_take(chess_board, "Rook", (4, 4), (0, 4))  # Same column

    assert not can_take(chess_board, "Rook", (4, 4), (5, 5))  # Diagonal move
    assert not can_take(chess_board, "Rook", (4, 4), (5, 6))  # Different row and column


def test_can_take_edge_of_board():
    chess_board = create_chess_board()
    assert can_take(chess_board, "Knight", (0, 0), (2, 1))
    assert can_take(chess_board, "Knight", (7, 7), (5, 6))
    assert can_take(chess_board, "Rook", (0, 0), (0, 7))
    assert can_take(chess_board, "Rook", (7, 7), (0, 7))


def test_can_take_invalid_white_piece():
    chess_board = create_chess_board()
    assert not can_take(chess_board, "Pawn", (4, 4), (5, 4))


def test_rook_blocked():
    chess_board = create_chess_board()
    place_piece(chess_board, 4, 4, "Rook", "White")  # Rook at e4
    place_piece(chess_board, 4, 6, "Pawn", "Black")  # Pawn at g4
    place_piece(chess_board, 6, 4, "Pawn", "Black")  # Pawn at e2

    assert can_take(chess_board, "Rook", (4, 4), (4, 6))  # Can take the pawn at g4
    assert not can_take(chess_board, "Rook", (4, 4), (4, 7))  # Can't take beyond the pawn at g4
    assert can_take(chess_board, "Rook", (4, 4), (6, 4))  # Can take the pawn at e2
    assert not can_take(chess_board, "Rook", (4, 4), (7, 4))  # Can't take beyond the pawn at e2
