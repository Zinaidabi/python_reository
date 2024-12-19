drink_name = "Lemon Tea"
drink_cost = 5.00

# print the menu

print("--------------")
print(drink_name, '=', drink_cost, "MDL / 100ml")
print("--------------")

# user enters volume
order_volume = input('enter desired volume: ') # '500' str

# "xs", "sm", "md", "lg"

# validation
if order_volume == "xs" or order_volume == "sm" or order_volume == "md" or order_volume == "lg" :

    # processing
    if order_volume == "xs":
        order_cost = 250 * drink_cost / 100
    if order_volume == "sm":
        order_cost =  330 * drink_cost / 100
    if order_volume == "md":
        order_cost = 500 * drink_cost / 100
    if order_volume == "lg":
        order_cost =750 * drink_cost / 100


    # output the result
    print(drink_name, 'x' , order_volume, 'ml =', order_cost)
    
else:
    print("order_volume should be only(xs, sm, md, lg) ml")

print("Thank you for using our service!")    