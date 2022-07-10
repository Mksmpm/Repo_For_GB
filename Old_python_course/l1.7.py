# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.


a = int(input('Input the first result in km: '))
b = int(input('Input the wanted result in km: '))
day = 1
if a >= b:
    print('Wrong input. Wanted result cannot be less than first result')
else:
    while a <= b:
        a = a + a * 0.1
        day += 1
    print(f"On the {day}th day the athlete will get the result of more than {b} km")
