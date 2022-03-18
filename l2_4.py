# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.
usr_str = str(input("Input the string with spaces: "))
usr_list = usr_str.split()

for word in usr_list:
    print(f"{usr_list.index(word) + 1} - {word[:10]}")
