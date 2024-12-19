
desination = input("enter destination: ")

if desination == 'job':
    print("You are here")
elif desination == "home" or desination == "market":
    print("forward R1->R2")
    desination = input ("enter destination: ")

    if desination == 'home':
        print("left R2-> S10")
        # R2 x S10
    elif desination == "market" :
        print("forward R1->S20")
        desination = input ("enter destination: ")

        if desination == 'market':
            print("You are here")
        elif desination == "home" :
            print("l S20->S11")

else:
    print("unknown")
    


