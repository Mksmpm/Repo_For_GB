# Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.

def pow_func(x, y):
    a = 1
    for i in range(abs(y)):
        a = a * x
    if y >= 0:
        return a
    else:
        return 1 / a


while True:
    inp_x = float(input('Введите действительное положительное число x: '))
    if inp_x <= 0:
        print('Введите  положительное число x!')
    else:
        while True:
            try:
                inp_y = int(input('Введите целое отрицательное число y: '))
                if inp_y >= 0:
                    print('Введите целое отрицательное число y!')
                else:
                    break
            except ValueError:
                print('Введите целое число y!')
        break

print(pow_func(inp_x, inp_y))
