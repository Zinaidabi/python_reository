# Remake 1d robo game -> for loop
from os import system
roboX = 5
roboHP = 100
roboBT = 100
Score = 0
bombX = 15
bombY = 3
heart = 10
coin  = 2



LENGTH = 20
option = ""

# game loop
while True:
    ################# 1. Draw Map ######################
    system("clear")
    print("\n")

    for x in range (1, LENGTH + 1):
        if x == roboX:
            print("⛄", end=" ")
        elif x == bombX:
            print("💣", end= " ")
        elif x == bombY:
            print("💣", end= " ")
        elif x == heart:
            print("💜", end= " ")
        elif x == coin:
            print("💰", end= " ")
        else :        
            print(".", end=" ")

    print("\nHP: ", roboHP)
    print("BT: ", roboBT, "%")
    print("Sc: ", Score)
    print("\n")
    ################# 1. Draw Map #######################

    ################# 2. READ INPUT #####################
    option = input(" >>> ")
    ################# 2. READ INPUT #####################

    ################# 3. Decide #########################
    if option == "a" and roboX > 1 :  # move left
        roboX -= 1
        roboBT -= 1
    if option == "d" and roboX < 20:   # move right
        roboX += 1
        roboBT -= 1
    # check
    if roboX == bombX:
        roboHP -= 10
        bombX = -1  # Remove bombX from the map
    if roboX == bombY:
        roboHP -= 10
        bombY = -1  # Remove bombY from the map
    if roboX == heart:
        roboHP += 10    # Increase HP
        heart = -1 # Remove heart from the map
    if roboX == coin:
        Score += 10    # Increase Score
        coin = -1 # Remove coin from the map

    if option == "x":  # exit
        print("Thank you for playing!")
        break
    ################# 3. Decide #########################

# HW1: Frontier check RIGHT
# HW2: place second bomb
# HW3: place some hearts -> HP+
# HW4: place some coins  -> score
# HW5: add variables  -> state of bombs, coins, ...

