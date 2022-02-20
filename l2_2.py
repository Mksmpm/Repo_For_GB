# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

user_list = []
list_len = int(input("Enter the number of elements for your list: "))

# Цикл для собирания списка
for i in range(list_len):
    el = input(f"Insert the element in your list: ")
    user_list.append(el)
print(f"Your original list: {user_list}")

# Делаем копию для перемешивания значений
user_lst_copy = user_list.copy()

# Цикл для перемешивания по четным элементам
for i in range(list_len):
    if (i + 1) % 2 == 0:
        user_list[i] = user_lst_copy[i - 1]
        user_list[i - 1] = user_lst_copy[i]

print(f"Your mixed list: {user_list}")
