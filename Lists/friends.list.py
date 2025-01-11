# FACT: list of friends
# emty list
friends = []
while len(friends) < 100:
    name = input("Add friend name: ")
    if name == "":
        break
    if name in friends:
        print("This name is already in the list")
    else:
    #HW1: check if the name is in the list
        friends.append( name )

print("You have", len(friends),"friends")
for i in range(len(friends)):
    print(" ", i, ">>", friends[i])