# you can ignore the "Unsolved Reference" errors
import pgzrun
from random import randint
from pgzhelper import *

# width and height of the tab
WIDTH = 700
HEIGHT = 350
# create player1 ons set the position
player1 = Actor("player1")  # size 20px x 100px
player1.x = 65
player1.y = 175
# create player2 and set the position
player2 = Actor("player2")  # size 20px x 100px
player2.x = 635
player2.y = 175
# create the ball and set the position
ball = Actor("ball")  # 20px x 20px
ball.x = 350
ball.y = 175
while True:
    ball.angle = randint(-180, 180)
    if ball.angle > 0 and 70 < ball.angle < 110 or ball.angle < 0 and -110 < ball.angle < -70:
        continue
    else:
        break
# points
player1_points = 0
player2_points = 0
# speed of the ball
speed = 2.5

def draw():
    # draw the elements of the game
    screen.fill((12, 12, 12))  # black background
    player1.draw()
    player2.draw()
    ball.draw()
    screen.draw.text(f"{player1_points} : {player2_points}", (330, 25))

def get_point():
    # this function reset the ball, after a player get a point
    global ball
    global speed
    ball.x = 350
    ball.y = 175
    while True:
        ball.angle = randint(-180, 180)
        if ball.angle > 0 and 70 < ball.angle < 110 or ball.angle < 0 and -110 < ball.angle < -70:
            continue
        else:
            break
    speed = 2.5


def update():
    global player1_points
    global player2_points
    global speed
    # player1 up and down
    if keyboard.w and player1.y > 50:
        player1.y -= 7
    if keyboard.s and player1.y < 300:
        player1.y += 7
    # player2 up and down
    if keyboard.up and player2.y > 50:
        player2.y -= 7
    if keyboard.down and player2.y < 300:
        player2.y += 7
    # points
    if ball.x < 0:
        player2_points += 1
        get_point()
    if ball.x > 700:
        player1_points += 1
        get_point()

    if ball.y < 10 or ball.y > 340:
        # bounce
        try:
            ball.angle = randint((ball.angle - 10) * -1, (ball.angle + 10) * -1)
        except ValueError:
            ball.angle = randint((ball.angle + 10) * -1, (ball.angle - 10) * -1)
    if ball.colliderect(player1):
        speed += 0.5
        if ball.angle > 0:
            ball.angle -= randint(85, 95)
        else:
            ball.angle += randint(85, 95)
    if ball.colliderect(player2):
        speed += 0.5
        if ball.angle > 0:
            ball.angle += randint(85, 95)
        else:
            ball.angle -= randint(85, 95)
    # let the ball move
    ball.move_forward(speed)


pgzrun.go()
