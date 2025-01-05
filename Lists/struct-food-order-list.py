# order info -> lists
order_food_names  = ["pizza", "salad", "soup"]
order_food_prices = [  75.00,   45.00,  15.00]
order_food_q      = [      2,       1,      2] 
# index                    0,       1,      2

#iterative print
for i in range (len(order_food_names)):
    print(i+1, order_food_names[i],order_food_prices[i], order_food_q[i])

# HW2: calculate total -> print()
total = 0
for i in range (len(order_food_names)):
    total += order_food_prices[i] * order_food_q[i]
print("Total:", total)
