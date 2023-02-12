
# you can ignore the unsolved reference errors
import pgzrun
import random
from datetime import datetime

# width and height of the screen
WIDTH = 500
HEIGHT = 700
# create Dudu
dudu = Actor('嘟嘟')
# set score to 0
score = 0
# starts the misic
music.play('背景音乐')

# direction for brick 2
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
    # put Dudu on the 3 brick
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
    # check if the game should stop or not
    if dudu.image == '嘟嘟':
        # every second you get 60 points
        score += 1
        on_brick = 0
        for b in bricks:
            # move the bricks upwards
            b.y -= 2.5 + score / 1200
            # brick 2 move from right to left and from left to right
            if b.image == '踏板2':
                b.x += direction
                if b.right >= WIDTH:
                    direction = -3
                elif b.left <= 0:
                    direction = 3
            # create a new brick if a brick is out of the screen
            if b.y < 0:
                n = random.randint(1, 4)
                b.image = '踏板' + str(n)
                b.y = HEIGHT
                min_x = b.width // 2
                max_x = WIDTH - b.width // 2
                b.x = random.randint(min_x, max_x)
        for b in bricks:
            # Dudu move upwards if he is on a brick
            if dudu.colliderect(b) and dudu.bottom < b.bottom:
                dudu.bottom = b.top
                on_brick = 1
                # sto the game when Dudu is on brick 4
                if b.image == '踏板4':
                    dudu.image = '嘟嘟哭'
                # Dudu move with brick 2 when he is on it
                if b.image == "踏板2":
                    dudu.x += direction

        if on_brick == 0:
            # if dudu is not on a brick, he falls down
            dudu.y += 8
        # if Dudu hit the bottom of the  screen the game will stop
        if dudu.bottom > HEIGHT or dudu.bottom <= 0:
            dudu.image = '嘟嘟哭'
        if keyboard.left:
            if dudu.left > 0:
                dudu.x -= 5
        if keyboard.right:
            if dudu.right < WIDTH:
                dudu.x += 5
    if dudu.image == '嘟嘟哭':
        try:
            f = open("penguin_game_point_history.txt", "a")
        except FileNotFoundError:
            f = open("penguin_game_point_history.txt", "w")
        now = datetime.now()
        f.write(f'{now.strftime("%d/%m/%Y %H:%M:%S")}    Points : {score} \n')
        # stops the music
        music.stop()


def on_key_down(key):
    # restart the game
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