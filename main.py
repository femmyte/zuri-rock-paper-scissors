import random
import time
option = ['R', 'P', 'S']


def printDelay(message):
    time.sleep(1)
    print(message)


def init():
    movement()
    user_move()


def user_move():
    move = input('Choose from the option to play \n "R" '
                 'for "rock", "P" for "paper", "S" for "scissors"').upper()

    return move


computer_move = ''
# comp_move = random.choice(option)
comp_move = 'R'
if comp_move == 'R':
    computer_move = 'Rock'
elif comp_move == 'S':
    computer_move = 'Scissors'
else:
    computer_move = 'Paper'

# user_move = user()


def score(player, computer):
    if(player == 'R' and computer == 'R') or (player == 'S' and computer == 'S') or (player == 'P' and computer == 'P'):
        print('Tie')
        user_move()
    elif(player == 'R' and computer == 'S') or (player == 'P' and computer == 'R') or (player == 'S' and computer == 'P'):
        return 'Player Won'
    elif(computer == 'R' and player == 'S') or (computer == 'P' and player == 'R') or (computer == 'S' or player == 'S'):
        return 'Computer Won'


while user_move() not in option:
    printDelay('Invalid move kindly enter the right option')
    user_move()


def movement():
    if(user_move() == 'R'):
        printDelay(f'Player (Rock) : Computer ({computer_move})')
        print(score(user_move(), comp_move))
    elif(user_move() == 'P'):
        printDelay(f'Player (Paper) : Computer ({computer_move})')
        print(score(user_move(), comp_move))
    elif(user_move() == 'S'):
        printDelay(f'Player (Scissors) : Computer ({computer_move})')
        print(score(user_move(), comp_move))


init()
