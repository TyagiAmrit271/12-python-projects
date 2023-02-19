#rock paper scissor game

import random
def play():
    user = input("Enter your choice 'r' for rock, 'p' for paper, 's' for scissor")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'tie'
    if is_win(user,computer):
        return 'you won'

    return 'you lose'

def is_win(player,opponent):
    if(player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent =='p'):
        return True

print(play())