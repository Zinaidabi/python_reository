# cars & gas stations
# 1. litres
# 2. money
# 3. km

# HW1: Set a variable with consume L/100km (10L/100km) 
#      Calculate and print distance

litters = int(input("how many litters?")) 
litters_cost = 25.00
consumtion = 10  #litters per 100 Km

bill = litters* litters_cost
distance =(litters/consumtion) * 100  # Km



print(bill)
print(distance)