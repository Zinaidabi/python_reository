# alloritm with simple and multiple lists

cases = [50,10, 100, 150, -1, -1, 50] # 7 cities  / -1 -> no data
# Alg1: calc total / sum of values
# s = cases[0] + cases[1]  cases[2] + cases[3] + cases[4]
s = 0
for c in cases:
    if c >= 0: 
        s += c
print("Total cases:" , s)

product_cat_prices = [0.50, 10.00, 1.50 , 2.50 ,5.50]

#Alg1:
discount = 0.9
for i in range(len(product_cat_prices)): 
    if product_cat_prices[i] > 5:
        product_cat_prices[i] = product_cat_prices[i]* discount

#Alg2: print + iter+ index
for i in range(len(product_cat_prices)):
    print( i,")", product_cat_prices[i])

# 5 star rating for users / int
rating = [5, 3, 4, 2, 3, 1, 4 ] # 7 users
print("Username|Rating")
#Alg1: inter + print + index
for i in range ( len(rating)):
    print("user", i + 1," =", rating[i], end=" ")

    for r in range(rating[i]):
        print("*", end="")
    print()        