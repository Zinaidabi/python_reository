# add content

from os import system
from time import sleep
ads = [
    "Buy this Python book for only 0.99$ ",    # 0
    "Try this course of Python for free!!!",   # 1
    "Drink a lot of water(2L per day minimum)" # 2
]
ads_duration = [
    3.0,
    6.0,
    8.0
]

# Method 1: index only
index = 0
while True:
    ad = ads[index]
    duration = ads_duration[index]
    system("clear")
    print(" >> ", ad ," << ")
    sleep(duration)  # Wait specific duration
    index += 1
    if index >= len(ads):  
        index = 0

# HW 1: apply the correct duration