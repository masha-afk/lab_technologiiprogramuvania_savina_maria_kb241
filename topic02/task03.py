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
     match op:
        case "+":
            return add(a, b)
        case "-":
            return subtract(a, b)
        case "*":
            return multiply(a, b)
        case "/":
            return divide(a, b)

a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
op = input("Введіть операцію (+, -, *, /): ")
result = calculator(a, b, op) 
print("Результат:", result)