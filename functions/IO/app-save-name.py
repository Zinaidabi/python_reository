name= input("Enter your name please: ")

file = open("name.txt", "w")
file.write(name)
file.close()