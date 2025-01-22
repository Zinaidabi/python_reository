items     = ["Marry", "Peter",] # this is what we search for
found     = [  False,  False]
container = ["John","Marry", "Bob"]   # where to look for
# index           0,      1,     2

for j in range(len(items)):
    for i in range(len(container)):
        found[j]  = container[i] == items[j] # bool (true/false) <-- remember
        if found[j]:
            break
   
#################################################
print(items)
print(found)
for j in range(len(items)):
    if found[j]:                 # check the memory
        print(items[j], "Found!")
    else:
        print(items[j], "Not found!")