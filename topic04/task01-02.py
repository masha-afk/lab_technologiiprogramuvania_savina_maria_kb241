def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "На нуль ділити не можна!"
    
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

print("Простий консольний калькулятор. Введіть 'вийти' або 'q' для завершення.")
while True:
    try:
        op = input("Введіть операцію (+, -, *, /) або 'вийти': ")
        if op == 'вийти' or op == 'q':
            print("Програма завершена. До побачення!")
            break 
        else:
            a = float(input("Введіть перше число: "))
            b = float(input("Введіть друге число: "))
            result = calculator(a, b, op) 
            print(f"Результат: {a} {op} {b} = {result}")
    except ValueError:
        print("Будь-ласка, використовуйте лише числа!")