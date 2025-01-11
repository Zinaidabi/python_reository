# Python DATA Structures:
# list = ordered collection / array
# 1. indexed
# 2. dynamic
# 3. typefree (hint: recomended - same type)

#  + iteration
############################################

days  = ['Mo','Tu','Wd','Th', 'Fr',  'Sa','Su']
temps = [10.0, 9.0, 8.0, 0.0, -5.0, -10.0, 0.0]

#           0,    1,  2,   3,    4, ...

for i in range (7):
    if temps[i] <= 0:
        sign = "☼"
    else:
        sign = " "
    print(sign,days[i], temps[i])