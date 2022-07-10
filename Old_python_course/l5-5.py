#  Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
#  Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
from random import randint

with open('les5.txt', 'w+', encoding='utf-8') as f_obj:
    for i in range(randint(1, 100)):
        f_obj.write(str(randint(1, 100)) + ' ')
    f_obj.seek(0)
    total_sum = sum(map(int, f_obj.read().split()))
print(total_sum)
