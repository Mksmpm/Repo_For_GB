# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

noun = int(input('Please type any positive number: '))
max_n = 0
while noun > 1:
    noun //= 10
    mod = noun % 10
    if mod > max_n:
        max_n = mod
print(f"Biggest digit in your number is {max_n}")
