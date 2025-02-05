def ii( which ):
    print("Enter", which, "integer: " , end= "")
    return int(input())

a = ii("first")
b = ii("second")

op = input("Choose operation(* / + - **)") # op = "+"

res = 0

if op == "+":
    res = a + b
elif op == "*":
    res = a * b
elif op == "/":
    res = a  / b
elif op == "-":
    res = a - b
elif op == "**":
    res = a ** b
else:
    res = "wrong operation"

print("Result: ", res)

## HW1. next operations: / - **, if the user choses an inexistent operation
## -> "wrong operation"
