
# value = input("Enter some value: ")

def inputInt(message):
    while True:
        return int(input(message))

def inputFloat(message):
    while True:
        return float(input(message))
        
def inputBoolean(message):
    while True:
        value = input(message).strip().lower()
        if value in ["true", "t", "yes", "y"]:
            return True
        elif value in ["false", "f", "no", "n"]:
            return False




b = inputBoolean("Enter a boolean value (True/False, Yes/No): ")
print(f"Boolean value: {b}")           
n = inputInt("Enter the first integer: ")
m = inputFloat("Enter the second integer: ")
print(n + m)