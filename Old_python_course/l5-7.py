# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

import json

with open('les7.json', 'w') as f_obj_w:
    with open('les7.txt', 'r', encoding='utf-8') as f_obj_r:
        income_dict = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_obj_r}
        avg_profit = sum([i for i in income_dict.values() if i >= 0]) / len([i for i in income_dict.values() if i >= 0])
        parsed_list = [income_dict, {"average_profit": int(avg_profit)}]
        print(parsed_list)
    json.dump(parsed_list, f_obj_w)


