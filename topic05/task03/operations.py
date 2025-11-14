from functions import add, subtract, multiply, divide

def operations(choice):
    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))

        match choice:
            case "1":
                print(f"Результат: {add(a, b)}")
            case "2":
                print(f"Результат: {subtract(a, b)}")
            case "3":
                print(f"Результат: {multiply(a, b)}")
            case "4":
                print(f"Результат: {divide(a, b)}")
                
    except ValueError:
        print("Використовуйте лише числа!")