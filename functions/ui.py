from os import system

def clear():
    system("clear")

def controls():
    print("use a,d,s,w - for directions")
    key = input(">> ")
    return key
