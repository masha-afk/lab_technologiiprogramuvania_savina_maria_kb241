def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return 
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

print("Простий консольний калькулятор. Введіть 'q' для завершення.")
while True:
        op = input("Введіть операцію (+, -, *, /) або 'вийти': ")
        if  op == 'q':
            print("Програма завершена. До побачення!")
            break 
        else:
            a = float(input("Введіть перше число: "))
            b = float(input("Введіть друге число: "))
            result = calculator(a, b, op) 
            print(f"Результат: {a} {op} {b} = {result}")
