# import randon for the computer player side.
import random
# import os that use clear off the screen
# to prevent repeating display sections.
import os
# import colored and termcolor for colors.
"""
I would like to both use import color and I want to
learning to vary color syntax.
"""
from colored import fg, bg, attr
from termcolor import colored

# store from the color options.
color_blue = fg('blue')
color_cyan = fg('cyan')
color_red = fg('red')
color_yellow = fg('yellow')
color_magenta = fg('magenta')
color_light_blue = fg('light_blue')
color_light_cyan = fg('light_cyan')
color_rosy_brown = fg('rosy_brown')


# For the head dispaly.
def header_logo():
    print(color_blue + "\t--------------------------------")
    print(colored("\t                                ", 'red', 'on_white'))
    print(colored("\t          Tic Tac Toe           ", 'red', 'on_white',
                                                        attrs=['bold']))
    print(colored("\t                                ", 'red', 'on_white'))
    print(color_blue + "\t--------------------------------\n")


# For the username to entry the box.
username = input(color_cyan + "What's your name?\n")
print("\n")


# When you entry name and output display on screen and included colors.
def print_message(username):
    print(f"\033[5;32m\tHello {username}\n\t" + color_yellow
          + "Welcome to Tic Tac Toe, \n")
    print(f"\t{fg(30)}{attr(1)} How do use play play rule: \n")
    print(f"\t{fg(62)}  - 'x' is your player")
    print(f"\t{fg(62)}  - 'o' is computer's player")
    print(f"\t{fg(62)}  - Only choose between 1 and 9")
    print(f"\t{fg(62)}  - when the winner is then",
          "there are either type 'yes' or 'no'\n")
    print(f"\t{fg(74)}  - Enjoy play tic tac toe!\n")


# the spots in the board.
board = ["*", "*", "*", "*", "*", "*", "*", "*", "*"]


# The displayboard create a grid box with the spot.
def display_board(board):
    print("\033[1;32m\t+---+---+---+")
    print("\t| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("\033[1;32m\t+---+---+---+")
    print("\t| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("\033[1;32m\t+---+---+---+")
    print("\t| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("\033[1;32m\t+---+---+---+")
    print("\n")


# The global for funtion as follows below:
currentplayer = "x"
winner = None
gamerunning = True

"""
The create the board for the players, check the board who is winner.
there are three sections for horizon lines, vertical lines and
across lines.
"""


def horizon_lines_winner(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "*":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "*":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "*":
        winner = board[6]
        return True


def vertical_lines_winner(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "*":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "*":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "*":
        winner = board[2]
        return True


def across_lines_winner(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "*":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "*":
        winner = board[2]
        return True


# The human player use 'x'.
def turn_player():
    global currentplayer
    if currentplayer == "x":
        currentplayer = "o"
    else:
        currentplayer = "x"


# The computer player use 'o'.
def computer(board):
    while currentplayer == "o":
        position = random.randint(0, 8)
        if board[position] == "*":
            board[position] = "o"
            turn_player()


# The check if there are tie.
def check_draw(board):
    """
    It was working before when I asked tutor because I found it have
    some glitch and I want to solution check_draw. we tried to figure it out
    what was problem.Unforunately, my time allowance was hit up. I ran to fix
    sereval times and could not find solution. My deadline was so closed then
    I stop to fix and move on to do ReadMe.
    """
    global gamerunning
    if "*" not in board:
        display_board(board)
        print(color_yellow + "\tIt's a tie!")
        gamerunning = False
        exit()


def who_winner():
    """
    To check who is winner, there are sections if the winner came up,
    to ask the user to play again yes or no and there is error handle
    when the type e.g 'n' then prompt to ask to correct type
    either 'yes' or 'no'.

    If the user type 'yes' then start contiune playing.

    If the user type 'no' then prompt to say "Goodbye! Come back to play again"
    """
    global board
    if (
        horizon_lines_winner(board)
        or vertical_lines_winner(board)
        or across_lines_winner(board)
    ):
        display_board(board)
        print(color_yellow + f"\tThe winner is {winner}.\n")
        while True:
            user_input = input(color_blue + "\tDo do you want"
                               + "to play again, type: yes or no: ")
            print('\n')
            if user_input.lower() == 'yes':
                # Use clear off the screen to prevent
                # repeating display sections.
                os.system("cls" if os.name == "nt" else "clear")
                board = ["*", "*", "*", "*", "*", "*", "*", "*", "*"]
                display_board(board)
                break
            elif user_input.lower() == 'no':
                print(color_magenta + "\tGoodbye!, Come back to play",
                      "again ;)\n")
                exit()
            else:
                print(color_rosy_brown + "\tplease use type",
                      "either 'yes' or 'no'.\n")


def player_input(board):
    """
    The user press to the number between 1 and 9.
    There is error handle when the type e.g '45' then
    prompt to ask to correct pick the number between 1 and 9.

    If the user type 'g' then the prompt ask to use the number

    If the user type pick the number where the player had taken
    then prompt to say "Oh the player have already taken" and
    let the human player choose to the spot themselve.
    """
    while True:
        try:
            x = int(input(color_yellow + "\tchoose the number"
                    + "between 1 and 9: "))
            if 1 <= x <= 9:
                if board[x - 1] == "*":
                    board[x - 1] = currentplayer
                    # Use clear off the screen to prevent repeating
                    # display sections.
                    os.system("cls" if os.name == "nt" else "clear")
                    break
                else:
                    print(color_cyan + "\tOh the player have already taken!\n")
            else:
                print(color_light_blue + "\tThere is over 9,",
                      "please pick the number between 1 and 9.\n")
        except ValueError:
            print(color_light_cyan + "\tInvalid input.",
                  "Please enter numbers between 1 and 9.\n")


# Use clear off the screen to prevent repeating display sections.
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def game_running():
    """
    These the functions called above to here running
    the game loops
    """
    # Display logo Tic Tac Toe.
    header_logo()
    # Display user name.
    print_message(username)
    # Call functions above to run loop the game.
    while gamerunning:
        # The grid board with the spot.
        display_board(board)
        # player pick numbers and included error handles.
        player_input(board)
        # The human player is turning for 'x'
        turn_player()
        # The winner will prompt either 'x' or 'o'
        who_winner()
        # The tie (mentioned above docstring to explained)
        check_draw(board)
        # The computer player is turning for 'o'
        computer(board)
        # To prevent repeating display sections.
        clear_screen()


game_running()
