# import randon for the computer player side
import random
import os
import colorama
from colored import fg

color_blue = fg('blue')
color_cyan = fg('cyan')
color_red = fg('red')
color_yellow = fg('yellow')
color_magenta = fg('magenta')



# for the head dispaly
def header_logo():
    print(color_blue + "\t--------------------------------")
    print(color_red + "\t         Tic Tac Toe       ")
    print(color_blue + "\t--------------------------------")


# for the username to fill the box
username = input(color_cyan + "What's your name?\n")
print("\n")



# when you fill the name and output display on screen
def print_message(username):
    print(color_blue + f"\tHello {username}\n\t" + color_yellow + "Welcome to Tic Tac Toe")


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
    print(color_magenta + "+---+---+---+")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print(color_magenta + "+---+---+---+")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print(color_magenta + "+---+---+---+")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print(color_magenta + "+---+---+---+")
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
        print(color_magenta + "It's a tie!")
        gamerunning = False
        exit()
        

def who_winner():
    global board
    if (
        horizon_lines_winner(board)
        or vertical_lines_winner(board)
        or across_lines_winner(board)
    ):
        display_board(board)
        print(color_magenta + f"The winner is {winner}.")
        while True:
            user_input = input(color_blue + 'Do do you want to play again, type: yes or no: ')
            if user_input.lower() == 'yes':
                board = ["*", "*", "*", "*", "*", "*", "*", "*", "*"]
                display_board(board)
                break            
            elif user_input.lower() == 'no':
                print(color_magenta + "Goodbye!, Come play back again ;)\n")
                exit()
            
    
        
def player_input(board):
    inp = int(input(color_magenta + "choose the number between 1 and 9: "))
    os.system("cls" if os.name == "nt" else "clear")
    if board[inp  -1] == "*":
        board[inp  -1] = currentplayer
    else:
        print(color_magenta + "Oh the player have already taken!")
        

def game_running():
    while gamerunning:
        header_logo()
        print_message(username)
        display_board(board)
        player_input(board)
        turn_player()
        who_winner()
        check_draw(board)
        computer(board)


game_running()