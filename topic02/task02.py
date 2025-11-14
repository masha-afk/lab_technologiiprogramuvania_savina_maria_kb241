def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Помилка! Ділення на нуль неможливе."
    else:
        return a / b

def calculator(a, b, op):
    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        return divide(a, b)
    else:
        return "Невідома операція"

a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
op = input("Введіть операцію (+, -, *, /): ")
result = calculator(a, b, op)
print("Результат:", result)