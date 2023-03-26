# Milestone Project 01
# Tic Tac Toe Game
# 2 Players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place
# a symbol on the board
# Use the number pad to match numbers to the grid on a tic-tac-toe board
game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


# Have a P1 and a P2 to choose X or O
def get_player():
    p1 = "none"
    p2 = "none"

    while p1 not in ['X', 'O']:
        p1 = input("Does Player 1 want to be X or O: ").upper()

        if p1 not in ['X', 'O']:
            print("Sorry that is an invalid selection, try again")
        elif p1 == 'X':
            p2 = 'O'
        elif p1 == 'O':
            p2 = 'X'
    return p1, p2


# Have a display function to print a board
def print_board(board):
    print(f"_{board[0]}_|_{board[1]}_|_{board[2]}_")
    print(f"_{board[3]}_|_{board[4]}_|_{board[5]}_")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")


# Update the list of characters for the board
def play_game(board):
    p1, p2 = get_player()
    playing = True

    while playing:
        print_board(board)

        print("Player 1: ")
        update_p1(p1)
        print_board(board)
        if win_check(board, p1):
            break
        if " " not in board:
            print("Tie Game!!!")
            break

        print("Player 2: ")
        update_p2(p2)
        print_board(board)
        if win_check(board, p2):
            break
        if " " not in board:
            print("Tie Game!!!")
            break

        user_action = stop_game()
        if user_action == "N":
            playing = False


# check input
def update_p1(p1):
    p1_input = get_input()
    game_board[p1_input - 1] = p1


def update_p2(p2):
    p2_input = get_input()
    game_board[p2_input - 1] = p2


# Check input
def get_input():
    user_input = ""
    valid_loc = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    while not user_input.isdigit():
        user_input = input("Please enter a location on the board that isn't taken between (1-9): ")

        if not user_input.isdigit():
            print("Please enter a valid location (1-9)")
        elif user_input.isdigit():
            if int(user_input) not in valid_loc:
                print("Please enter a valid location (1-9")
                user_input = ""
            elif game_board[int(user_input) - 1] != " ":
                print("Location already taken try again")
                user_input = ""

    return int(user_input)


# Loop the game until users choose to end the game
def stop_game():
    user_input = ""
    while user_input not in ['Y', 'N']:
        user_input = input("Do you want to keep playing Yes(Y), No(N): ").upper()

    return user_input


# Check if won
def win_check(board, player):
    # Check all rows
    if (board[0] == player) and (board[1] == player) and (board[2] == player):
        print(f"{player} Wins!!!!")
        return True
    elif (board[3] == player) and (board[4] == player) and (board[5] == player):
        print(f"{player} Wins!!!!")
        return True
    elif (board[6] == player) and (board[7] == player) and (board[8] == player):
        print(f"{player} Wins!!!!")
        return True

    # Check all columns
    elif (board[0] == player) and (board[3] == player) and (board[6] == player):
        print(f"{player} Wins!!!!")
        return True
    elif (board[1] == player) and (board[4] == player) and (board[7] == player):
        print(f"{player} Wins!!!!")
        return True
    elif (board[2] == player) and (board[5] == player) and (board[8] == player):
        print(f"{player} Wins!!!!")
        return True

    # Check 2 diagonals
    elif (board[0] == player) and (board[4] == player) and (board[8] == player):
        print(f"{player} Wins!!!!")
        return True
    elif(board[6] == player) and (board[4] == player) and (board[2] == player):
        print(f"{player} Wins!!!!")
        return True
    else:
        return False


play_game(game_board)
