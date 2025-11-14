def find_insert_position(sorted_list, new_value):
    for i in range(len(sorted_list)):
        if new_value < sorted_list[i]:
            return i
    return len(sorted_list)
lst = [2, 4, 6, 8, 10]
new_element = 7
position = find_insert_position(lst, new_element)
print(f"Елемент {new_element} слід вставити на позицію {position}")