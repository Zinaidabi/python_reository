from time import sleep
from os import system


#Data Input

e_what = input("Event type: ")
e_where = input("Event location: ")
e_when = input("Event time: ")

system("clear")
sleep(3)

# Data output
print("\n\n\n")
print("Atention!!!")
print("You have a", e_what, e_where, " at",e_when,  "hours")

