# Step 1
# x ---- R ----- >
# CONTROLS: "a" - left, "d" - right
from os import system

LENGHT = 20
roboX = 5

direction = ""
# game loop
while direction != "x":
    system ("clear")
    # ########### DRAW THE MAP #############
    print("\n")
    x = 1
    while x <= LENGHT:
        if x == roboX:
            print("R", end="")   #"\n"
        else:
            print("-", end="")   #"\n"
        x += 1
    print("\n")  

    # ########### DRAW THE MAP #############
    # ########### CONTROLS #############
    direction = input("dir(a/d) >>> ")
    if direction == "a":
        roboX -= 1
    if direction == "d":
        roboX += 1

    # ########### CONTROLS #############

      

