# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой

def usr_info(**kwargs):
    print(str(kwargs).strip('{}'))  # Вывод данных о пользователе одной строкой


# def usr_inputs():
#    usr_list = ['name', 'surname', 'date_of_birth', 'city', 'email', 'phone']
#    usr_data = {}
#    for i in usr_list:
#        usr_data[i] = input(f'Input your {i}: ')
#    usr_inp = str(usr_data).replace(':', ' =').replace('\'', '').strip('{}')
#    usr_info(usr_inp)
# Не вышло сделать итеративное заполнение именнованых аргументов с инпута в функцию usr_info(**kwargs)


usr_info(name='Maks', surname='Melnik', date_of_birth='10-10-1992', city='Spb',
         email='somemail@gmail.com', phone='999-0101-202')
