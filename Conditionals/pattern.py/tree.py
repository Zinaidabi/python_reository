  
height = 11
for row in range (1,height + 1): #1,2,3,4,5
   spaces = height + 1 - row
   triangles = row
   if row % 2 == 0:  
        print(" " * spaces + "◉ " + "▲ " * (triangles - 2) + "◉")
   else:
        print( " " * spaces + "▲ " * triangles)

print(" " * height + "▮")

# HW*1: add lights on each even row sides