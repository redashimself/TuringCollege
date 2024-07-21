from main import map_letter_to_board_column_coordinate
from main import map_number_to_board_row_coordinate
from main import place_piece
from main import create_chess_board
from main import process_piece_placement_input
from main import can_take


def test_map_letter_to_board_column_coordinate():
    assert map_letter_to_board_column_coordinate("Knight e5") == 4
    assert map_letter_to_board_column_coordinate("Knight a5") == 0


def test_map_number_to_board_row_coordinate():
    assert map_number_to_board_row_coordinate("Knight e1") == 7
    assert map_number_to_board_row_coordinate("Knight e4") == 4
    assert map_number_to_board_row_coordinate("Knight a8") == 0


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
    assert can_take("Knight", (4, 4), (6, 5))
    assert can_take("Knight", (4, 4), (6, 3))
    assert can_take("Knight", (4, 4), (2, 5))
    assert can_take("Knight", (4, 4), (2, 3))
    assert can_take("Knight", (4, 4), (5, 6))
    assert can_take("Knight", (4, 4), (5, 2))
    assert can_take("Knight", (4, 4), (3, 6))
    assert can_take("Knight", (4, 4), (3, 2))

    assert not can_take("Knight", (4, 4), (4, 5))  # Adjacent square
    assert not can_take("Knight", (4, 4), (6, 6))  # Diagonal move
    assert not can_take("Knight", (4, 4), (7, 7))  # Far away


def test_can_take_rook():
    assert can_take("Rook", (4, 4), (4, 7))  # Same row
    assert can_take("Rook", (4, 4), (4, 0))  # Same row
    assert can_take("Rook", (4, 4), (7, 4))  # Same column
    assert can_take("Rook", (4, 4), (0, 4))  # Same column

    assert not can_take("Rook", (4, 4), (5, 5))  # Diagonal move
    assert not can_take("Rook", (4, 4), (5, 6))  # Different row and column


def test_can_take_edge_of_board():
    assert can_take("Knight", (0, 0), (2, 1))
    assert can_take("Knight", (7, 7), (5, 6))
    assert can_take("Rook", (0, 0), (0, 7))
    assert can_take("Rook", (7, 7), (0, 7))


def test_can_take_invalid_white_piece():
    assert not can_take("Pawn", (4, 4), (5, 4))
