# Create functions that correspund to: + - * /

# Pure functions

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def sub(a, b):
    return a - b

def add(a, b):
    return a + b



r = add(10, 100)
print(r)

result = add(1, div(mul(2, 3), 4))
print(result)  

# HW2: Rewrite r = 1 + 2 * 3 / 4