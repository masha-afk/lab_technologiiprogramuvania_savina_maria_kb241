from operations import operations

def main():
    while True:
        print("\n--- Калькулятор ---")
        print("1. Додавання")
        print("2. Віднімання")
        print("3. Множення")
        print("4. Ділення")
        print("5. Вихід")

        choice = input("Оберіть операцію (1-5): ")

        if choice == "5":
            print("Вихід з програми...")
            break
        else:
            operations(choice)
if __name__ == "__main__":
    main()
