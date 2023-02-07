# Pgzrun-games
Some little games using pgzrun and some other (mostly built-in) libraries
***
## What does the project do?
This is a project with some mini-games, which is code in Python and mostly using the pgzrun-libary. Every game has his own folder and in every folder there are a txt file, with the source of the picture or other things I downloaded. In the Images folder of each game, there are the pictures of the items in the game.
***
## What do i need to install?
You need to install pgzrun, type this in your Shell/Terminal:

`pip install pgzrun`
***
## Flappy Angry Birds
In this game, you can choose one of the bird from the game "Angry Birds". I you do not know, what are the names from the birds, you can look in the "Image" folder. After that, you must choose, if you want to hold or to click  "SPACE" for flying resp. jumping. Then the game will start in 5 seconds. You must dodge the wood blocks. In the top-left corner, there is the scoreboard. Evry time when a wood block leaves the screen, you get a point. If you get hit by a wood block, the game will stop and your points will be saved in the point history. This is a txt file, where you can look the exact date and hour when you die up and there will be the  points of this try too.
##### Source
Source of the Images:


https://www.angrybirds.com/characters/red/
https://www.angrybirds.com/characters/chuck/
https://www.angrybirds.com/characters/bomb/
https://www.angrybirds.com/characters/bubbles/
https://www.angrybirds.com/characters/hal/
https://www.angrybirds.com/characters/blues/
https://www.angrybirds.com/characters/mighty-eagle/
https://www.angrybirds.com/characters/terence/
https://www.angrybirds.com/characters/matilda/
https://www.angrybirds.com/characters/stella/

https://www.pinterest.de/pin/77546424806129711/
https://pymunk-tutorial.readthedocs.io/en/latest/bird/bird.html
https://www.nicepng.com/ourpic/u2w7e6e6a9o0y3i1_angry-bird-backgrounds-background-game-angry-bird/
https://www.deviantart.com/damienfan/art/angry-birds-background-900745105

https://pymunk-tutorial.readthedocs.io/en/latest/bird/bird.html
***
## Ping-Pong game
This game is a a two-player game. The left player can move his/ her paddle with "W" (up) and "S" (down) and the right player con move his/ her paddle with the up and down button. In top-middle is the scoreboard. Every time, a playe cannot hit the ball, the other player get a point. If you hit the ball with the upper resp. lower side of the paddle, you can let he ball make very interesting moves.


You can add in the update function thes following lines, to let player1 and player2 spin:

```
player1.angle += 100
player2.angle += 100
# you can use any integer or float value
```

##### Source
https://www.pngitem.com/middle/hwJmwox_neon-blue-light-circle-tumblr-neon-lights-tumblr/
https://www.pngitem.com/middle/wTThoR_neon-rectangle-freetoedit-frame-border-geometric-parallel-hd/
https://www.pngitem.com/middle/whmThJ_neon-rectangle-freetoedit-red-frame-border-geometric-hd/
https://www.aposteriori.com.sg/pygame-zero-helper/

The file "pgzhelper.py", I downloaded from the last link.
***
