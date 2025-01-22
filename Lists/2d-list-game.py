from os import system
import random
option = ' '
robo_r = 0
robo_c = 0

rows, cols = 5, 5

gmap = [
    ['x', ' ', ' ', ' ', ' '],  # 0
    [' ', ' ', ' ', ' ', ' '],  # 1
    [' ', ' ', ' ', ' ', ' '],  # 2
    [' ', ' ', ' ', ' ', ' '],  # 3
    [' ', ' ', ' ', ' ', ' '],  # 4
    # 0,   1,   2,    3,   4
]

def place_mines(gmap, num_mines=3):
    mines = 0
    while mines < num_mines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        if gmap[r][c] == ' ':  # Asigură-te că mina nu este plasată pe robot
            gmap[r][c] = '*'  # Plasează mina
            mines += 1
place_mines(gmap)           

while option != 'x':
##########Print the map ########
    system("clear")
    print("-"*12)
    for r in range(5):

        print ("|", end="")
        for c in range(5):
            print(gmap[r][c], end=" ")
        print("|")
    print("-"*12)
    print("\n\nControls: \na -left\nd -right\nw -up\ns -down\nx -exit")
###### Print the map ##########

    ###### Controls ##########
    option = input(">>")
    if option == 'd':
        if robo_c < 4:
            gmap[robo_r][robo_c] = ' ' # remove from current position
            robo_c += 1
            if gmap[robo_r][robo_c] == '*':
                print("Game Over!")
                break
            gmap[robo_r][robo_c] = 'x'  # place it on the new position

    if option == 's':
        if robo_r < 4:
            gmap[robo_r][robo_c] = ' ' # remove from current position
            robo_r += 1
            if gmap[robo_r][robo_c] == '*':
                print("Game Over!")
                break
            gmap[robo_r][robo_c] = 'x'  # place it on the new position

    if option == 'a':
        if robo_c > 0: 
            gmap[robo_r][robo_c] = ' ' # remove from current position
            robo_c -= 1
            if gmap[robo_r][robo_c] == '*':
                print("Game Over!")
                break
            gmap[robo_r][robo_c] = 'x' # place it on the new position

    if option == 'w':
        if robo_r > 0: 
            gmap[robo_r][robo_c] = ' ' # remove from current position
            robo_r -= 1
            if gmap[robo_r][robo_c] == '*':
                print("Game Over!")
                break
            gmap[robo_r][robo_c] = 'x' # place it on the new position

    ###### Controls ##########
    #HW1: Add movement to left, up
    #HW2: Add limits
    #HW3: Add mines + Game over conditions