people = ["Johny", "Marry", "Francis"]  # top 3 developers in a company
# index         0,       1,         2
print("Before", people)
# triangle
# temp      = people[0]  # "Johny"
# people[0] = people[1]  # "Marry" -> "Johny"
# people[1] = temp       # "Johny" -> "Marry"

name_to_move = input("Enter the name of the person to move: ")
current_index = people.index(name_to_move)
new_position = int(input(f"Enter the new position for {name_to_move} (0-{len(people) - 1}): "))
if new_position < 0 or new_position >= len(people):
    print("Error: Position out of bounds.")
else:
    temp = people[new_position]
    people[new_position] = people[current_index]
    people[current_index] = temp

print("After", people)
# HW1: add code -> user -> placeA, placeB
# HW2: check boundaries