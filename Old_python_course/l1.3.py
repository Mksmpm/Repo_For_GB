# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = str(input('Type one number from 0 to 9: '))
sum_num = int(number) + int(number * 2) + int(number * 3)
print(f"{number} + {number * 2} + {number * 3} = {sum_num}")
