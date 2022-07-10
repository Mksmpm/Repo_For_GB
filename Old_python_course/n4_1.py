# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

sc_name, salary_per_h, working_hours, premium = argv

print(f'Зарплата в час = {salary_per_h}')
print(f'Часов отработано = {working_hours}')
print(f'Премия = {premium}')

salary = (int(salary_per_h) * int(working_hours)) + int(premium)

print(f'Заработано: {salary}')

input('Press ENTER to exit')
