# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

seconds = int(input('Please, insert the time in seconds: '))
hh = seconds // 60 // 60
mm = seconds // 60 % 60
ss = seconds % 60
print(f"Translated time is: {hh}:{mm}:{ss}")
