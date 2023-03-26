# Milestone Project
# Exercises
# Displaying Information
def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


top_row = [" ", " ", " "]
mid_row = [" ", " ", " "]
bot_row = [" ", " ", " "]
display(top_row, mid_row, bot_row)


# Accepting User Input
def user_choice():
    choice = "WRONG"
    acceptable_range = range(0, 10)
    within_range = False

    while not choice.isdigit() or not within_range:
        choice = input("Please enter a number (0-10): ")

        if not choice.isdigit():
            print("Sorry that is not a digit!")
        if choice.isdigit():
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Sorry, you are out of acceptable range (0-10)")

    return int(choice)


user_choice()

# Simple User Interaction
game_list = [0, 1, 2]


def display_game(game_list):
    print("Here is the current game list")
    print(game_list)


def position_choice():
    choice = "wrong"

    while choice not in ["0", "1", "2"]:
        choice = input("Pick a position to replace (0, 1, 2):")

        if choice not in ["0", "1", "2"]:
            #clear_output()
            print("Sorry, but you did not choose a valid position (0, 1, 2)")

    return int(choice)


def replacement_choice(game_list, position):
    user_placement = input("Type a string to a place at the position")
    game_list[position] = user_placement
    return game_list


def gameon_choice():
    choice = "wrong"

    while choice not in ['Y', 'N']:
        choice = input("Would you like to keep playing? Y or N ")

        if choice not in ['Y', 'N']:
            #clear_output()
            print("Sorry, I didn't understand.  Please make sure you choose Y or N.")

    if choice == 'Y':
        return True
    else:
        return False


game_on = True

while game_on:
    #clear_output()
    display_game(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list, position)

    #clear_output()
    display_game(game_list)

    game_on = gameon_choice()
