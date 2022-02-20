# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.

while True:
    try:
        usr_month = int(input("Enter the month as a number 1-12: "))
        if usr_month in range(1, 12):
            break
        else:
            print("Wrong input. Number in range 1-12 expected")
    except ValueError:
        print("Wrong input. Number expected")

# Через dict
month_dict = {
    (1, 2): "Winter",
    (11, 12): "Winter",
    (3, 4): "Spring",
    (5, 8): "Summer",
    (9, 10): "Autumn"
}
for (k1, k2) in month_dict:
    if k1 <= usr_month <= k2:
        print(month_dict[k1, k2])

# Через list
month_list = [
    "Winter",
    "Winter",
    "Spring",
    "Spring",
    "Summer",
    "Summer",
    "Summer",
    "Summer",
    "Autumn",
    "Autumn",
    "Winter",
    "Winter"
]
print(month_list[usr_month - 1])
