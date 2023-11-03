# from tkinter import Entry
from module import *

player1score = 0
player2score = 0

print("\n=== JACKPOT ===\n")

while True:
    print("player1's turn")

    if Entry() == "":
        if Game():
            player1score += 1
            print("you won")
        else:
            print("you lost")
    else:
        print("Wrong input!!")
    print("=========================")

    print("player2's turn")

    if Entry() == "":
        if Game():
            player2score += 1
            print("you won")
        else:
            print("you lost")
    else:
        print("Wrong input!!")
    print("Player1 ", end="")
    player1decision = decision()
    print("Player2 ", end="")
    player2decision = decision()

    if (player1decision == "n") and (player2decision == "n"):
        print("Well played")

        print("player1 score : ", player1score)

        print("player2 score : ", player2score)

        break
