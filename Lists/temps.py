# list
weekly_temps = [
    -1,  32,  -1,   0,   10,  20,  31
]
weekly_days = [
    'Mo','Tu','Wd','Th','Fr','Sa','Su'
]

# control / loops
for i in range(len(weekly_temps)):
    # f strings
    print(f"{weekly_days[i]}: {weekly_temps[i]:5}", end = " ")
    # control / branching
    if weekly_temps[i] < 0:
        print("☼")
    elif weekly_temps[i] > 30:
        print("🔥")
    else:
        print()
# HW1: for temperature over 30 -> display "🔥"