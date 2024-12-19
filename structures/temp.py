print("Enter temperatures >")

day_1_temp = int(input("day 1:"))
day_2_temp = int(input("day 2:"))
day_3_temp = int(input("day 3:"))
day_4_temp = int(input("day 4:"))
day_5_temp = int(input("day 5:"))
day_6_temp = int(input("day 6:"))
day_7_temp = int(input("day 7:"))

week_temp = (day_1_temp + day_2_temp + day_3_temp + day_4_temp + day_5_temp + day_6_temp + day_7_temp) / 7

print("avg weekly temp: " , week_temp)

