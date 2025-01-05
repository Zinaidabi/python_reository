from os import system
# draw this triangle

#HW1: size from keyboard

#        +
#      + + +
#    + + + + + 
#  + + + + + + +
#+ + + + + + + + +

system("clear")

# print(". . +")         0  # 2 / 1
# print(". + + +")       1  # 1 / 3
# print("+ + + + +")     2  # 0 / 5

size = int(input("Enter the size of the pyramid: "))

n = 0
while n < size :
    print("  " * (size - n - 1) + "+ " * (2 * n + 1) )
    n += 1