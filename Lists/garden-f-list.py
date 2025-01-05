# parking lot
p    = [None, None, "BMW", None, "Mercedes", None, "BMW"] # list of None type
# index    0,    1,     2,    3,        4,        5,     6

user_car_brand  = input("Name your brand:")
user_park_index = int(input("What place:?"))
if p[user_park_index] == None:
   print("Ok, you can park there!!!")
   p[user_park_index] = user_car_brand
else:("This place is occupied!!!")
#free / total
total = len(p)
free = 0 
for i in range(len(p)):
    if p[i] == None:
      free += 1  
print("Parking (free/total):",free, "/", total, "places")

for i in range(len(p)):
   print(i,p[i])

# HW1: Calculate / print stats:
# "Mercedes" -1
# "BMW" - 2
# "Toyota" 1
brand_stats = {}
for car in p:
   if car is not None:
      if car in brand_stats:
         brand_stats[car] += 1
      else:
         brand_stats[car] = 1
for brand, count in brand_stats.items():
   print(f"{brand} - {count}")
   
brands_to_check = ["Mercedes", "BMW", "Toyota"]
for brand in brands_to_check:
    if brand not in brand_stats:
        print(f"{brand} - 0")
