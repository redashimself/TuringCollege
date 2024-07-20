game_board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

empty_cells = []

for row in range(3):
    for col in range(3):
        if game_board[row][col] == ' ':
            empty_cells.append((row, col))

print(empty_cells)



# row_index = 0
    # cell_index = 0
    # computer_made_choice = False
    # for row in game_board:
    #     if computer_made_choice:
    #         break
    #     if cell_index == 3:
    #         row_index += 1
    #         cell_index = 0
    #
    #     for cell in row:
    #         if computer_made_choice:
    #             break
    #         if cell == ' ' and computer_side == "x":
    #             computer_choice_randomized = random.choice([' ', 'x'])
    #             user_input = f"{computer_choice_randomized}{row_index}{cell_index}"
    #             update_game_board(game_board, user_input)
    #
    #             if user_input[0] == ' ':
    #                 cell_index += 1
    #                 continue
    #             elif len(user_input[0]) > 0:
    #                 computer_made_choice = True
    #                 continue
    #         else:
    #             cell_index += 1