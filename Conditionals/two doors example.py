PIN_DOOR_1 = "0123"
PIN_DOOR_2 = "4321"

# user input

pin_door_1 = input("Enter first pin: ")
lock_1_open = pin_door_1 == PIN_DOOR_1  

if lock_1_open:
    print("I'm in the building") 

    pin_door_2 = input("Enter second pin: ")
    lock_2_open = pin_door_2 == PIN_DOOR_2 

    if lock_2_open:
        print("I'm in the flat")
    else:
        print("Incorrect pin. Wait 2 minutes and try again")      
else:
        print("Incorrect pin. Wait 2 minutes and try again")   