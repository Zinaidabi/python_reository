# real data < source: API, Database, Keyboard, File, ...
meeting_presense = [
    "Alexandru",
    "Alex",
    "Stefan",
    "Habib",
    "Livia",
    "Viktor",
    "X",
    "serghei",
    "Stepan"
]

print("Students present at the meeting: ", len(meeting_presense) ) 
for s in meeting_presense:
    print(s)
name = input("Who? ")
for s in meeting_presense:
    if s == name:
        print(name, "found!!!")