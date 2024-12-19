
import random

bf_period_start = 22
bf_period_end = 29

# HW: input from kb

current_date = 3 # < from keyboard

# HW2: set random values between 0...5

random_number = random.randint(1, 5)
print(f"Random number: {random_number}")

views_per_last_hour = random_number

if views_per_last_hour < 5:
    if bf_period_start <= current_date <= bf_period_end:
         print("BLACK FRIDAY discounts upto - 50%!!!")
# else


