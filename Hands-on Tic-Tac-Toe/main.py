# Create a 2d array that represents tic tac toe board [x]
# Display the board [x]
# Accept user input (human) [x]
# Validate user input [x]
# Change the board state based on input [x]
# Display the board state [x]
# Create a random input for the computer [x]
# Write conditions when the game is over (winning/tie conditions) [x]
# Loop the game till it's over [x]
# Implement computer having to pick a move (make the empty tile random) [x]
# Print out which player won [x]

import random


def create_empty_game_board():
    return [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]


def user_input_is_not_valid(user_input):
    if (not user_input.startswith("x")
            and not user_input.startswith("o")
            or len(user_input) != 3
            or int(user_input[1]) > 2
            or int(user_input[2]) > 2):
        return True
    return False


def print_game_board(game_board):
    for row in game_board:
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print()


def update_game_board(game_board, user_input):
    row = int(user_input[1])
    column = int(user_input[2])

    game_board[row][column] = user_input[0]


def is_win(game_board):
    for row in game_board:
        if row == ["x", "x", "x"] or row == ["o", "o", "o"]:
            return True

    for col in range(3):
        if (game_board[0][col] == game_board[1][col] == game_board[2][col] == "x" or
                game_board[0][col] == game_board[1][col] == game_board[2][col] == "o"):
            return True

    if (game_board[0][0] == game_board[1][1] == game_board[2][2] in ["x", "o"] or
            game_board[0][2] == game_board[1][1] == game_board[2][0] in ["x", "o"]):
        return True

    return False


def is_tie(game_board):
    for row in game_board:
        if " " in row:
            return False
    return True


def make_computer_move(computer_side, game_board):
    empty_cells = []

    for row in range(3):
        for col in range(3):
            if game_board[row][col] == ' ':
                empty_cells.append((row, col))

    if empty_cells:
        row, col = random.choice(empty_cells)
        game_board[row][col] = computer_side
        print("Board after computer made its move:")
        print_game_board(game_board)
        return True

    return False


def main():
    game_board = create_empty_game_board()
    current_player = "human"

    while True:
        if current_player == "human":
            user_input = input(
                "Make your move in [x/o][row_number][column_number] format e.g. x00 for top left x: ").strip().lower()

            if user_input_is_not_valid(user_input):
                print("You entered incorrect input, please restart the game")
                break

            update_game_board(game_board, user_input)
            print_game_board(game_board)

            player_side = user_input[0]

            if player_side == "x":
                computer_side = "o"
            else:
                computer_side = "x"
        else:
            make_computer_move(computer_side, game_board)

        if is_tie(game_board):
            print("It's a tie!")
            print_game_board(game_board)
            break
        elif is_win(game_board):
            print(f"{current_player} player won!")
            print_game_board(game_board)
            break

        current_player = "computer" if current_player == "human" else "human"


main()
