import random

bf_period_start = 22
bf_period_end = 29

car_price = 12000          # the normal price of the car 
car_price_discount = 9600  # the price of the car in BLACK FRIDAY period

current_date = 3

# HW2: set random values between 0...5
random_number = random.randint(1, 5)
print(f"Random number: {random_number}")

views_per_last_hour = random_number

if bf_period_start <= current_date <= bf_period_end:
    if views_per_last_hour <= 5:
        print("BLACK FRIDAY discounts upto - 20%!!!")
        print(f"Discounded car price: {car_price_discount}")

else:
    print(f"Car price is: {car_price}")


