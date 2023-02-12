# you can ignore the unsolved reference errors
import pgzrun
import random
from datetime import datetime

# set width and height of the screen
WIDTH = 500
HEIGHT = 700
# create the penguin
dudu = Actor('嘟嘟')
# set score to 0
score = 0
# stars th misic
music.play('背景音乐')
# direction var for a brick
direction = 3
# create the bricks
bricks = []
for i in range(5):
    n = random.randint(1, 4)
    b = Actor('踏板' + str(n))
    min_x = b.width // 2
    max_x = WIDTH - b.width // 2
    b.x = random.randint(min_x, max_x)
    b.y = 140 * (i + 1)
    bricks.append(b)
    # put the penguin o the 3 brick
    if i == 2:
        dudu.x = b.x
        dudu.bottom = b.top
        b.image = '踏板1'


def draw():
    # draw all elements of the game
    global score
    screen.blit('背景', [0, 0])
    dudu.draw()
    for brick in bricks:
        brick.draw()
    # scoreboard
    screen.draw.text(str(score), (20, 10))


def update():
    global score, direction
    # if you die, the game will stop
    if dudu.image == '嘟嘟':
        # evry second you get 60 points
        score += 1
        on_brick = 0
        for b in bricks:
            # move the bricks up
            b.y -= 3
            # move brick 2 from left to right and from right to left
            if b.image == '踏板2':
                b.x += direction
                # change direction
                if b.right >= WIDTH:
                    direction = -3
                elif b.left <= 0:
                    direction = 3
            if b.y < 0:
                # random brick
                n = random.randint(1, 4)
                b.image = '踏板' + str(n)
                b.y = HEIGHT
                min_x = b.width // 2
                max_x = WIDTH - b.width // 2
                b.x = random.randint(min_x, max_x)

                if dudu.colliderect(b) and dudu.bottom < b.bottom:
                    # check if the penguin is on a brick
                    dudu.bottom = b.top
                    on_brick = 1
                    # if the penguin is on brick 4, the game will stop
                    if b.image == '踏板4':
                        dudu.image = '嘟嘟哭'
                    # if the penguin is on brick 2 it, the penguin will move in the same direction as the brick 2
                    if b.image == "踏板2":
                        dudu.x += direction

        if on_brick == 0:
            dudu.y += 8
        # if the penguin is on the ground the game will stop
        if dudu.bottom > HEIGHT:
            dudu.image = '嘟嘟哭'
        # move the penguin
        if keyboard.left:
            if dudu.left > 0:
                dudu.x -= 5
        if keyboard.right:
            if dudu.right < WIDTH:
                dudu.x += 5

    if dudu.image == '嘟嘟哭':
        # write the points in the point history
        try:
            f = open("penguin_game_point_history.txt", "a")
        except FileNotFoundError:
            f = open("penguin_game_point_history.txt", "w")
        now = datetime.now()
        f.write(f'{now.strftime("%d/%m/%Y %H:%M:%S")}    Points : {score} \n')
        # stop the misic
        music.stop()


def on_key_down(key):
    # play again
    if key == keys.SPACE and dudu.image == '嘟嘟哭':
        global score, bricks
        music.play('背景音乐')
        dudu.image = '嘟嘟'
        bricks = []
        score = 0
        for i in range(5):
            n = random.randint(1, 4)
            b = Actor('踏板' + str(n))
            min_x = b.width // 2
            max_x = WIDTH - b.width // 2
            b.x = random.randint(min_x, max_x)
            b.y = 140 * (i + 1)
            bricks.append(b)
            if i == 2:
                b.image = '踏板1'
                dudu.x = b.x
                dudu.bottom = b.top


pgzrun.go()
