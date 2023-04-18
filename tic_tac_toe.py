def the_game():
    """The 'tic-tac-toe' game for two players.
    Both players move successively until one of them wins or the game ends with a tie."""

    board = ['_'] * 9

    def printing_board(filled_board):
        # For printing the nice board which will be shown to users
        pretty_board = "   |   |   \n" \
                       "---*---*---\n" \
                       "   |   |   \n" \
                       "---*---*---\n" \
                       "   |   |    "
        pretty_board = list(pretty_board)
        # Dict compares the indexes from the board with the indexes from the pretty_board
        dict_index = {0: 1, 1: 5, 2: 9, 3: 25, 4: 29, 5: 33, 6: 49, 7: 53, 8: 57}
        idx = -1
        for x in filled_board:
            idx += 1
            if x == 'X':
                pretty_board[dict_index[idx]] = 'X'
            elif x == 'O':
                pretty_board[dict_index[idx]] = 'O'
        return ''.join(pretty_board)

    def diagonal_win(game_board):
        # Check if someone won on the diagonal lines.
        if game_board[4] == game_board[0] == game_board[8] or game_board[2] == game_board[4] == \
                game_board[6]:
            if game_board[4] != '_':
                return game_board[4]
        return False

    def horizontal_win(game_board):
        # Check if someone won on the horizontal lines.
        for x in range(0, 9, 3):
            if game_board[x] == game_board[x + 1] == game_board[x + 2] and game_board[x] != '_':
                return game_board[x]
        return False

    def vertical_win(game_board):
        # Check if someone won on the vertical lines.
        for x in range(3):
            if game_board[x] == game_board[x + 3] == game_board[x + 6] and game_board[x] != '_':
                return game_board[x]
        return False

    def if_someone_win(game_board):
        # Check if someone already won or not.
        if horizontal_win(game_board):
            return horizontal_win(game_board)

        elif diagonal_win(game_board):
            return diagonal_win(game_board)

        elif vertical_win(game_board):
            return vertical_win(game_board)

    def play_again(user_answer):
        # If users want to play again
        if user_answer.upper() not in ['YES', 'NO']:
            play_again(input("The answer is incorrect. You should type 'yes' or 'no': /n>>> "))
        elif user_answer.upper() == 'YES':
            the_game()
        else:
            print("OK. Bye bye!")

    def game(g_board, player, position):
        # Function with the right game.
        if position in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            # Check if the user input is correct (number from 1 to 9)
            position = int(position) - 1
            if player == player1:
                g_board[position] = 'X'
            else:
                g_board[position] = 'O'

        else:
            return False

    print("\nHello players!\nThis is a tic-tac-toe game. Let's start!\n" + "-" * 30 + "\n\n")

    player1 = input("Player 1 type your name:\n>>> ")
    player2 = input("Player 2 type your name:\n>>> ")

    print(
        f"\nHello players! {player1} has a sign 'X' and {player2} has a sign 'O'. "
        f"You can choose the location from 1 to 9. "
        f"{player1} you start!\n")

    print(printing_board(board))
    print("\n")

    game_continue = True

    while game_continue:

        if if_someone_win(board):
            print(f"{player2} won!!!")
            break

        else:

            move_p1 = input(f"{player1} type your number: ")

            while game(board, player1, move_p1) is False:
                # Check if the place chosen by the player1 is already filled or the input is wrong.
                print("Your choice is wrong. Try again! ")
                print(f"{printing_board(board)}\n")
                move_p1 = input(f"{player1} type your number: ")

            else:

                print(f"{printing_board(board)}\n")
                if not if_someone_win(board):
                    move_p2 = input(f"{player2} type your number: ")

                    while game(board, player2, move_p2) is False:
                        # Check if the place chosen by the player2 is already filled or the input is wrong.
                        print("Your choice is wrong. Try again! ")
                        print(f"{printing_board(board)}\n")
                        move_p2 = input(f"{player2} type your number: ")

                    else:

                        print(f"{printing_board(board)}\n")
                else:

                    print(f"{player1} won!!!")
                    game_continue = False

    play_again(input(f"\nDo you want to play again? Type 'yes' or 'no'.\n>>> "))


the_game()