# Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

revenue = int(input('Input your company revenue: '))
losses = int(input('Input your company losses: '))
profit = revenue - losses

if profit > 0:
    margin = (profit / revenue) * 100
    print(f"Your profit is {profit} and margin is {margin:.2f}%")
    employees = int(input('Type the number of your employees: '))
    prof_per_emp = profit / employees
    print(f"You have {prof_per_emp:.1f} per employee")
else:
    print('Sorry to hear you have a negative income :(')
