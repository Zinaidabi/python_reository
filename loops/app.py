from os import system

q = ['1','2','3','4','5','6', '7','X']
x_index = 7

while True:
    system('clear')

    print('  C')
    print('  V')

    print('   ', end=" ")

    for i in range(len(q)):
        print(q[i], end=" ")

    # print("<--------------------- direction")  HW: make this by using loop    
    print()
    direction = "<"
    for _ in range(25):  
        direction += "-"
    direction += " direction"
    print(direction)
    print()

    answer = input('move to front? (y/n)')
    # HW2: Limit movement beyond first position
    if answer == 'y' and x_index > 0:

        t = q[x_index-1]
        q[x_index-1] = q[x_index]
        q[x_index] = t
        x_index -= 1 
  