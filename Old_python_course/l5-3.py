#  Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
#  (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
#  Выполнить подсчёт средней величины дохода сотрудников


with open('les3.txt', 'r', encoding='utf-8') as f_obj:
    salary_dict = {}
    for el in f_obj:
        lst = el.split()
        salary_dict[lst[0]] = int(lst[1])

print('List of employees with salary less than 20k: ')
for name, salary in salary_dict.items():
    if int(salary) < 20000:
        print(f'{name} - salary {salary}')

avg_sal = round(sum(salary_dict.values()) / len(salary_dict), 2)
print('*' * 30)
print(f'Average salary - {avg_sal}')
