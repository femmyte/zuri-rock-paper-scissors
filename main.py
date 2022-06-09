import random

import time

option = ['R', 'P', 'S']


def printDelay(message):
    time.sleep(1)
    print(message)


def playerMove():
    player = input('Choose from the option to play \n "R" '
                   'for "rock", "P" for "paper", "S" for "scissors"').upper()
    if player not in option:
        print('Invalid movement, try again')
        # playerMove()
        init()
    return player


def computerMove():
    computer = random.choice(option)
    return computer


def score(player, computer):
    if ((player == 'R' and computer == 'S') or
        (player == 'S' and computer == 'P') or
            (player == 'P' and computer == 'R')):
        print("** YOU WON **")
    elif ((computer == 'R' and player == 'S') or
            (computer == 'S' and player == 'P') or
            (computer == 'P' and player == 'R')):
        print("** COMPUTER WON **")
    elif ((player == 'R' and computer == 'R') or
            (player == 'S' and computer == 'S') or
            (player == 'P' and computer == 'P')):
        print("** TIE **")
        init()


def init():
    computer = computerMove()
    score(playerMove(), computer)


init()
