from map import *
from ui import *

warning_msg = "" 

while True:
    clear()
    printMap( gameMap )

    if warning_msg:
        print(warning_msg)

    key = controls()

    if key == 'x':
        break


    gameMap[rr][rc] = 0  # initial position

    if key == 'd':
        if rc < 8 and (gameMap[rr][rc+1] == 3 or gameMap[rr][rc+2] == 3): 
            warning_msg = "Warning, 💣 detected!"
        elif rc < 9 and gameMap[rr][rc+1] != 1:
            rc += 1 
            warning_msg = ""         

    if key == 'a'and rc > 0 and gameMap[rr][rc-1] != 1:
        rc -= 1   
   
    if key == 's'and rr < 9 and gameMap[rr+1][rc] != 1:
        rr +=1

    if key == 'w'and rr > 0 and gameMap[rr-1][rc] != 1:
        rr -= 1

    gameMap[rr][rc] = 2 

# Hw1: add up and down movement
# Hw2: boundaries check right -> 9, left - 0
# Hw3: add some mines, when moving right -> rc+1,rc+2  - not a mine
#      in case of danger - > Warning -> danger detected
    