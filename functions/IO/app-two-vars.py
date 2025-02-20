file = open("data.txt", "r")
data = file.read()  # str type
name_1, name_2 = data.split(" ")

print(name_1)
print(name_2)
# print(f"|{data}|")
# print(names)