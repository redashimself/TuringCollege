from main import map_letter_to_board_column_coordinate
from main import map_number_to_board_row_coordinate
from main import get_piece_array_indices
from column_coordinate import Column


def test_map_letter_to_board_column_coordinate():
    assert map_letter_to_board_column_coordinate("Knight e5") == 4
    assert map_letter_to_board_column_coordinate("Knight a5") == 0


def test_map_number_to_board_row_coordinate():
    assert map_number_to_board_row_coordinate("Knight e1") == 7
    assert map_number_to_board_row_coordinate("Knight e4") == 4
    assert map_number_to_board_row_coordinate("Knight a8") == 0


def test_get_piece_array_indices():
    assert get_piece_array_indices("Knight e1") == 7
    assert get_piece_array_indices("Rook e4") == 4
    assert get_piece_array_indices("Pawn a8") == 0
