# import randon for the computer player side
import random
import os
from colored import fg, bg, attr
from termcolor import colored

color_blue = fg('blue')
color_cyan = fg('cyan')
color_red = fg('red')
color_yellow = fg('yellow')
color_magenta = fg('magenta')
color_light_blue = fg('light_blue')
color_light_cyan = fg('light_cyan')
color_rosy_brown =fg('rosy_brown')



# for the head dispaly
def header_logo():
    print(color_blue + "\t--------------------------------")
    print(colored("\t                                ", 'red', 'on_white'))
    print(colored("\t          Tic Tac Toe           ", 'red', 'on_white', attrs=['bold']))
    print(colored("\t                                ", 'red', 'on_white'))
    print(color_blue + "\t--------------------------------\n")


# for the username to fill the box
username = input(color_cyan + "What's your name?\n")
print("\n")



# when you fill the name and output display on screen
def print_message(username):
    print(f"\033[5;32m\tHello {username}\n\t" + color_yellow + "Welcome to Tic Tac Toe, \n")
    print(f"\t{fg(30)}{attr(1)} How do use play play rule: \n")
    print(f"\t{fg(62)}  - 'x' is your player")
    print(f"\t{fg(62)}  - 'o' is computer's player")
    print(f"\t{fg(62)}  - Only choose between 1 and 9")
    print(f"\t{fg(62)}  - when the winner is then, there are either type 'yes' or 'no'\n")
    print(f"\t{fg(74)}  - Enjoy play tic tac toe!\n")
    
"""
The displayboard create a grid box
"""

board = ["*", "*", "*", "*", "*", "*", "*", "*", "*"]


"""
The displayboard create a grid box with the number
and the run loop for a created grid board and come
from varible call board with the arrays
"""


def display_board(board):
    print("\033[1;32m\t+---+---+---+")
    print("\t| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("\033[1;32m\t+---+---+---+")
    print("\t| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("\033[1;32m\t+---+---+---+")
    print("\t| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("\033[1;32m\t+---+---+---+")
    print("\n")


# output grid with number of the board
# displayboard()

"""
The gamer turn to X or O onto the grid board

"""


currentplayer = "x"
winner = None
gamerunning = True


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
    

def turn_player():
    global currentplayer
    if currentplayer == "x":
        currentplayer = "o"
    else:
        currentplayer = "x"


def computer(board):
    while currentplayer == "o":
        position = random.randint(0, 8)
        if board[position] == "*":
            board[position] = "o"
            turn_player()


def check_draw(board):
    global gamerunning
    if "*" not in board:
        display_board(board)
        print(color_yellow + "\tIt's a tie!")
        gamerunning = False
        exit()


def who_winner():
    global board
    global gamerunning
    if (
        horizon_lines_winner(board)
        or vertical_lines_winner(board)
        or across_lines_winner(board)
    ):  
        display_board(board)
        print(color_yellow + f"\tThe winner is {winner}.\n")
        while True:
                user_input = input(color_blue + '\tDo do you want to play again, type: yes or no: ')
                print('\n')
                if user_input.lower() == 'yes':
                    os.system("cls" if os.name == "nt" else "clear")
                    board = ["*", "*", "*", "*", "*", "*", "*", "*", "*"]
                    display_board(board)
                    break
                elif user_input.lower() == 'no':
                    print(color_magenta + "\tGoodbye!, Come back to play again ;)\n")
                    exit()
                else:
                    print(color_rosy_brown + '\tplease use type either "yes" or "no".\n')
                    gamerunning = False
                
                    
def player_input(board):
    while True:
        try:
            x = int(input(color_yellow + "\tchoose the number between 1 and 9: "))
            if 1 <= x <= 9:
                if board[x - 1] == "*":
                    board[x - 1] = currentplayer
                    os.system("cls" if os.name == "nt" else "clear")
                    break
                else:
                    print(color_cyan + "\tOh the player have already taken!\n")
            else:
                print(color_light_blue + "\tThere is over 9, please pick the number between 1 and 9.\n")
        except ValueError:
            print(color_light_cyan + "\tInvalid input. Please enter numbers between 1 and 9.\n")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
            

def game_running():
    header_logo()
    while gamerunning:
        print_message(username)
        display_board(board)
        player_input(board)
        turn_player()
        who_winner()
        check_draw(board)
        computer(board)
    

game_running()