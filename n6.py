# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

# def capital_func(text: str):
#    return text.capitalize()
# print(capital_func('mama'))

# Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().


def func_capitalize(text: str):
    text_list = text.split()
    cap_list = []
    for word in text_list:
        cap_list.append(word.capitalize())
    new_str = ' '.join(cap_list)
    return new_str


def easy_capitalize(text: str):
    return text.title()


print(func_capitalize('some text to test our func'))
print(easy_capitalize('some text to test our func'))
