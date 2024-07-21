from main import map_letter_to_board_column_coordinate
from main import map_number_to_board_row_coordinate
from main import place_piece
from main import create_chess_board
from main import process_piece_placement_input
from column_coordinate import Column


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
    assert col == Column.e.value
    assert piece == "Knight"

    # Test bottom left
    row, col, piece = process_piece_placement_input("Rook a1")
    assert row == 7
    assert col == Column.a.value
    assert piece == "Rook"

    # Test top right
    row, col, piece = process_piece_placement_input("Queen h8")
    assert row == 0
    assert col == Column.h.value
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
