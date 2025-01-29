#  *  *  *
#  *  *  *
#  *  *  *

def printStar():
    print('*', end=' ')

def printStarRow(w):
    for i in range(w):
        printStar()
    print()

def printStarRect(w,h):
    if w > 0 and h > 0:
        for i in range(h):
            printStarRow(w)
    else:
        print('Dimensions cannot be negative!')
       
########################

printStarRect(3,3)

# HW1: draw the complete diagram

#    |
#    v
#   call ----> printStarRect(w=3,h=3)
#                  v
#                  v
#      Loop (h=3)  i: 0,1,2  --------------------------------------------------------|
#           |       v                                                                |
#           |       v                                                                |
#           |    call ----> printStarRow(w=3) ---------------------------------------|
#           |                   v                                                    |
#           |                    v                                                   |
#           |        Loop(w=3)  i: 0,1,2  -------------------------------------------|
#           |           |       v                                                   ||
#           |           |       v                                                   ||
#           |           |       call  -----> call printStar()                       ||
#           |           |                              v                            ||
#           |           |                              v                            ||
#           |           |                              call  ----> print('*')       ||
#           |           |                               <----------                 ||
#           |           <-----------  <----------------                             ||
#           |                                                                        |
#           <-------------------------------------------------------------------------
#   
#           <-------------------------------------------------------------------------
#
#