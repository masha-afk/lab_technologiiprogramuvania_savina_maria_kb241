def test_dict_functions():
    dict = {'a': 1, 'b': 2, 'c': 3}
    print("--- Тестування методів словника ---")
    print(f"Початковий словник: {dict}")

    print("Метод: keys() - повертає ключі словника")
    dict_keys = dict.keys()
    print(f"Результат: {dict_keys}")

    print("Метод: values() - повертає значення словника")
    dict_values = dict.values()
    print(f"Результат: {dict_values}")

    print("Метод: items() - повертає ключ та значення словника")
    dict_items = dict.items()
    print(f"Результат: {dict_items}")
    
    update_data = {'d': 4}
    print(f"Метод: update({update_data}) - додає пару з іншого словника")
    dict.update(update_data)
    print(f"Результат: {dict}")

    print("Оператор: del dict['c'] - видаляє елемент за ключем 'c'")
    del dict['c']
    print(f"Результат: {dict}")

    print("Метод: clear() - видаляє всі пари ключ-значення зі словника")
    dict.clear()
    print(f"Результат: {dict}")

test_dict_functions()