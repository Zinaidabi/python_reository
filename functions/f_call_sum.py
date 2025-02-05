## Create & call a function tat sums 3 integers - returns the result

def sum(a,b,c):
    s = a + b + c
    return s


# global variable
res = sum(1,2,3)
print(res)

#    ---> sum(1,2,3) ---------
#         |   |   |
#         v   v   v
#         1   2   3
#         v   v   v
#---- function sum(a,b,c) ----
#         |  s = a + b + c  |
#        -------------------
#               |
#           return s
#               |
#               v
# res = s  <-----
# |
# |
# v
# print( res )