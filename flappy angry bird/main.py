# you can ignore the "Unresolved reference 'Actor' 'screen' 'keyboard'"Errors
import pgzrun
from time import sleep
from datetime import datetime
from random import randint, seed

while True:
    """This block of code check, if you
    are choosing a bird, which is available.
     If you choose one, which is not available
     the programm let you try it again"""

    try:
        bird = Actor(input("Which bird do you want to play (for example Red or Chuck) ?").lower())   # bird size
        break                                                                                        # 100px x 100px
    except KeyError:
        print("No bird with this name. Try it again")
        sleep(2)
while True:
    """This block of code check, if you use holding space for flying.
    If not, you fly by press space every time.If your answer cannot be 
    interpreted if it is yes or no, the programm will ask you agai"""

    hold = input("Do you want to hold space for flying (Y/N)?")
    if "y" in hold.lower() or "n" in hold.lower():
        break
    print("ERROR. Try it again")

print("Game Starts in 5s")  # wait 5 second, so you can prepare for the game
sleep(5)
points = 0
start = 0
WIDTH = 1203  # width and height of the gametab
HEIGHT = 600
bg1 = Actor("background")  # background size 2560px x 1440px
bg1.x = 0
bg2 = Actor("background")  # 2 times the backround for animation
bg2.x = 601.5
bird.y = 300
bird.x = 100
#  in the list columns, thre are the wood blocks you must dodge in this game
columns = [Actor("column"), Actor("column"), Actor("column"), Actor("column")]  # column size  23px x 100px
for i in range(4):
    columns[i].x = 1250 + 300 * i
    columns[i].y = randint(75, 525)  # creating the wood block
def draw():
    # draw everything we need for the game
    bg1.draw()
    bg2.draw()
    bird.draw()
    # using for-loop for draw the wood blocks
    for c in columns:
        c.draw()
    # draw the scoreboard in the top-left corner of the game tab
    screen.draw.text(str(points), (20, 20))

def on_key_down(key):
    # if hold = no
    if key.SPACE and bird.y > 50 and "n" in hold.lower():
        bird.y -= 85
def update():
    global bird
    global start
    global points
    #  if hold = yes
    if keyboard.space and bird.y > 50 and "y" in hold.lower():
       bird.y -= 7.5
    for c in columns:
        c.x -= 2 + points / 4
        if bird.colliderect(c) or bird.y > 550:
            #  write informations in the point history, if you die
            try:
                f = open("flappyangrybird_point_history.txt", "a")
            except FileNotFoundError:
                f = open("flappyangrybird_point_history.txt", "w")
            now = datetime.now()
            f.write(f'{now.strftime("%d/%m/%Y %H:%M:%S")}    Points : {points} \n')
            exit()  # exit the game
        # if a wood block is not on the tab anymore
        if c.x < -23.5:
            points += 1
            seed()
            c.x = 1250
            c.y = randint(150, 525)
    # backroundanimation
    bg1.x -= 7
    bg2.x -= 7
    if bg1.x < -601.5:
        bg1.x = bg2.x + 1203
    if bg2.x < -601.5:
        bg2.x = bg1.x + 1203

    bird.y += 4.5


pgzrun.go()
