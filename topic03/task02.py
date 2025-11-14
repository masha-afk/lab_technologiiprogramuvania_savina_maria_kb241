def test_list_functions():
    lst = [1, 2, 3]
    print("--- Тестування методів списку ---")
    print(f"Початковий список: {lst}")

    print("Метод: extend([4, 5]) - додає елементи іншого списку")
    lst.extend([4, 5])
    print(f"Результат: {lst}")

    print("Метод: append(6) - додає один елемент в кінець")
    lst.append(6)
    print(f"Результат: {lst}")

    print("Метод: insert(2, 8) - вставляє 8 на індекс 2")
    lst.insert(2, 8)
    print(f"Результат: {lst}")

    print("Метод: remove(5) - видаляє 5")
    lst.remove(5)
    print(f"Результат: {lst}")

    print("Метод: sort() - сортує список за зростанням")
    lst.sort()
    print(f"Результат: {lst}")

    print("Метод: reverse() - змінює порядок на зворотний")
    lst.reverse()
    print(f"Результат: {lst}")

    print("Метод: copy() - створює поверхневу копію списку")
    copy_lst = lst.copy()
    print(f"Результат копії (copy_lst): {copy_lst}")
 
    print("Метод: clear() - видаляє всі елементи")
    lst.clear()
    print(f"Результат (lst): {lst}")
test_list_functions()