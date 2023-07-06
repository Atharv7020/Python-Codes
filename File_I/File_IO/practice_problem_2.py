#The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file "highscore.txt" which is either blank or contains the previous highscore you need to write a program to update a highscore whenever game() breaks a highscore.
def game():
    score= 114
    return score


points=game()

with open('highscore.txt') as f:
    highscore=int(f.read())


if highscore<points:
    with open("highscore.txt",'w') as f:
        f.write(str(points))