# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]

while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("Wrong input. Number expected")

if num <= my_list[len(my_list) - 1]:
    my_list.append(num)
else:
    for i in my_list:
        if num > i:
            my_list.insert(my_list.index(i), num)
            break
        else:
            pass
print(f"Result: {my_list}")
