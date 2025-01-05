#   ---------
#   |   |   |
#   |   |   |
#   |-------|
#   |   |   |
#   |   |   |
#   ---------
#  HW1: add middle v/h lines

from os import system
system("clear")
print()

w = int(input('width: '))
h = int(input('height: '))

for r in range(h):
    for s in range(w):
        if r == 0 or r == h - 1:
            print("--", end = "")
        elif s == 0:
            print("| ", end = "")
        elif s == w - 1:
            print(" |", end = "")
        elif r == int(h / 2):
            print("--", end = "")
        elif s == int(w / 2):
            print("| ", end = "")   
        else:
            print("  ", end = "")
    print()

print()
