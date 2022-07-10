# 6. Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.


from itertools import count, cycle

for i in count(3):
    if i > 10:
        break
    else:
        print(i)

my_list = ['McDonalds', 'KFC', 'Burger King', 'Carlos Junior']

my_iter = cycle(my_list)
i = 0


for el in my_iter:
    print(el)
    i += 1
    if i >= 10:
        break
