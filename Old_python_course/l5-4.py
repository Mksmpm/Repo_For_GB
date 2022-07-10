# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

ru_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open('les4_rus.txt', 'w', encoding='utf-8') as f_rus:
    with open("les4.txt", 'r', encoding='utf-8') as f_orig:
        for ln in f_orig:
            f_rus.write(ln.replace(ln.split()[0], ru_dict.get(ln.split()[0])))

