# Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие
# лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.

hours_dict = {}
with open('les6.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        d_name = line.split(':')[0]
        les = [i for i in line.split(':')[1] if i.isdigit() or i == ' ']
        lessons_sum = sum(map(int, "".join(les).split()))
        # print(f'{d_name} - {lessons_sum}')
        hours_dict[d_name] = int(lessons_sum)

print(hours_dict)
