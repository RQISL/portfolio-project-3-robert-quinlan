# import randon for the computer player side
import random


# when you fill the name and output display on screen
def print_message(name):
    print(f"\nHello {name}\nWelcome to Tic Tac Toe")


# for the head dispaly
print("\t--------------------------------")
print("\t         Tic Tac Toe       ")
print("\t--------------------------------")

# for the username to fill the box
username = input("What's your name?\n")
print_message(f"{username}\n")
print("\n")


"""
The displayboard create a grid box
"""

board = ["*", "*", "*", "*", "*", "*", "*", "*", "*"]


"""
The displayboard create a grid box with the number
and the run loop for a created grid board and come
from varible call board with the arrays
"""


def displayboard(board):
    print("+---+---+---+")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("+---+---+---+")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("+---+---+---+")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("+---+---+---+")
    print("\n")


# output grid with number of the board
# displayboard()

"""
The gamer turn to X or O onto the grid board

"""


currentPlayer = "x"
winner = None
gameRunning = True


def PlayerInput(board):
    inp = int(input("choose the number between 1 and 9"))
    if inp >= 1 and inp <= 9 and board[inp - 1]:
        board[inp - 1] = currentPlayer
    else:
        print("oh you have already spot!")


def Horizon_Lines_Winner(board):
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


def Vertical_Lines_Winner(board):
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


def Across_lines_Winner(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "*":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "*":
        winner = board[2]
        return True


def check_Draw(board):
    global gameRunning
    if "*" not in board:
        displayboard(board)
        print("It's a tie!")
        gameRunning = False


def whoWinner():
    if (
        Horizon_Lines_Winner(board)
        or Vertical_Lines_Winner(board)
        or Across_lines_Winner(board)
    ):
        print(f"The winner is {winner}.")


def turnPlayer():
    global currentPlayer
    if currentPlayer == "x":
        currentPlayer = "o"
    else:
        currentPlayer = "x"


def computer(board):
    while currentPlayer == "o":
        position = random.randint(0, 8)
        if board[position] == "*":
            board[position] = "o"
            turnPlayer()


while gameRunning:
    displayboard(board)
    PlayerInput(board)
    check_Draw(board)
    whoWinner()
    turnPlayer()
    computer(board)
    check_Draw(board)
