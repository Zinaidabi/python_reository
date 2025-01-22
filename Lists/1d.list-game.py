from os import system


# HW1: if + condition ---> move right/ left - limits
# HW2: add variable hp = 100, each time danger hp - 50 -> when it's zero --> game over

hp = 100
option = ' '
over = False # bool
robo_x = 5  #coord
gmap = ['⚠', ' ', ' ', ' ', '□', ' ', ' ', ' ', ' ', '⚠']  # list: the map -> 10 values
# index  0, 1,...


while option!= 'x':
    ###### Print the map ##########
    system ("clear")
    print("-"*20)
    for i in range(len(gmap)):
        print(gmap[i], end =" ")
    print()
    print("-"*20)
    for i in range(len(gmap)):
        print(i, end =" ")
    print(f"\n\nHP: {hp}")    
    print("\n\nControls: a - left, d - right, x- exit")
###### Print the map ##########

###### Controls ##########
    if over:
        print("You failed!!!")
        break
    option = input (">>")
    if option == 'a':
        if robo_x > 0:
            gmap[robo_x] = ' ' #remove from current position
            robo_x -= 1
            if gmap[robo_x] == '⚠':
                hp -= 50
                if hp <= 0:   
                    gmap[robo_x] = '💀'
                    over = True
            else:
                gmap[robo_x] = '□' # place it on the new position
        else:
            gmap[robo_x] = '□'
            
    if option == 'd':
        if robo_x < len(gmap) - 1:
            gmap[robo_x] = ' ' # remove from current position
            robo_x += 1
            if gmap[robo_x] == '⚠':
                hp -= 50
                if hp <= 0:
                    gmap[robo_x] = '💀'
                    over = True
            else:
                gmap[robo_x] = '□' # place it on the new position
        else:
            gmap[robo_x] = '□'
            
    elif option == 'x':
        print('Game over')
        
    ###### Controls ##########   