# Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.

def add_sum(my_str: str) -> int:
    int_list = my_str.split(' ')
    my_sum = 0
    for i in range(len(int_list)):
        my_int = int(int_list[i])
        my_sum = my_sum + my_int
    return my_sum


total_sum = 0
while True:
    print('Чтобы завершить программу нажмите q')
    a = input('Введите числа разделенные пробелом: ').rstrip(' ')
    if a.upper() == 'Q':
        break
    else:
        total_sum = total_sum + add_sum(a)
    print(f"Сумма чисел на данный момен = {total_sum}")
