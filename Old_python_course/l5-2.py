#  Создать текстовый файл (не программно), сохранить в нём несколько строк,
#  выполнить подсчёт строк и слов в каждой строке.

with open('les2.txt', 'r', encoding='utf-8') as f_obj:
    print('*' * 30)
    print(f'File \'{f_obj.name}\' contains {len(f_obj.readlines())} line(s)')
    f_obj.seek(0)
    i = 0
    for line in f_obj:
        i += 1
        print(f'{i} line - contains {len(line.split())} words')
