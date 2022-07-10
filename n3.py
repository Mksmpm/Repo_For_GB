# Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    my_list = [a, b, c]
    my_sum = 0
    my_list.remove(min(my_list))
    for i in range(len(my_list)):
        my_sum += my_list[i]
    return my_sum


print(my_func(2, 4, 9))
