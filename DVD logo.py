import time
import os
import math
import random

dvdLogo = ["▓▓▓▓  ▓     ▓ ▓▓▓▓ ", \
           "▓   ▓  ▓   ▓  ▓   ▓", \
           "▓   ▓   ▓ ▓   ▓   ▓", \
           "▓▓▓▓     ▓    ▓▓▓▓  "]
colors = ['\033[95m', '\033[94m', '\033[96m', '\033[92m', '\033[93m', '\033[91m']
screenWidth = 120
screenHeight = 30
speed = 0.2
delay = 0.0005
angle = 45


def draw(posx, posy, imgwidth, imgheight):
    s = ""
    for y in range(screenHeight + 1):
        if (y <= posy and y > posy - imgheight):
            x = 0
            while x < screenWidth:
                if x > posx - imgwidth:
                    if x <= posx:
                        s += dvdLogo[y - (posy - imgheight) - 1][x - (posx - imgwidth) - 1]
                    else:
                        break
                else:
                    s += " "
                x += 1
        if (y < screenHeight):
            s += '\n'
    print(colors[colorIndex], s, end='')


def setRandomColor(color):
    tmp = color
    while tmp == color:
        color = random.randrange(0, 6)
    return color


posx = 40
posy = 8
imgwidth = len(dvdLogo[0])
imgheight = len(dvdLogo)
colorIndex = random.randrange(0, 6)

while (True):
    screenWidth, screenHeight = os.get_terminal_size()
    posy += math.sin(angle / 57.2958) * speed
    posx += math.cos(angle / 57.2958) * speed

    clearConsole = False
    if int(posy) >= screenHeight or int(posy) <= imgheight:
        angle = 360 - angle
        colorIndex = setRandomColor(colorIndex)
        clearConsole = True
    if int(posx) >= screenWidth - 1 or int(posx) < imgwidth:
        angle = 180 - angle
        colorIndex = setRandomColor(colorIndex)
        clearConsole = True

    posx = max(min(posx, screenWidth - 1), imgwidth - 1)
    posy = max(min(posy, screenHeight), imgheight)

    draw(int(posx), int(posy), imgwidth, imgheight)
    time.sleep(delay)
    if (clearConsole):
        os.system('cls')

