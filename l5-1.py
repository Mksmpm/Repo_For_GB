# Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.

with open('les1.txt', 'w', encoding='utf-8') as f_obj:
    while True:
        line = input('Input the line into the file. To exit just press enter: ')
        if line == '':
            print('Work finished. Closing the file')
            break
        else:
            f_obj.write(line + '\n')
