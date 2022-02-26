# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.

revenue = int(input('Input your company revenue: '))
losses = int(input('Input your company losses: '))

if revenue > losses:
    print('Good to hear you have a positive income')
else:
    print('Sorry to hear you have a negative income :(')
