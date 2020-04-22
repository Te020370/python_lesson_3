import pymorphy2
morph = pymorphy2.MorphAnalyzer()
# Тип данных СТРОКА
# Инициализация

temp_str = 'Марка авто "Volvo"'
temp_str = 'Марка авто \'Volvo\''
temp_str = 'Марка авто \\Volvo\\'
temp_str = ""
temp_str = 'Марка авто \\Volvo\\'
print(temp_str)

# Обращение к символам, подстрокам
# Вывод строки по символьно
for i in range(len(temp_str)):
    print(temp_str[i])
# Срезы
print(temp_str [1:])
print(temp_str [:4])
print(temp_str [1:4])
print(temp_str [1:-3])

# Функции со строками
print(temp_str, len(temp_str))

# Операции со строками
temp_str_2 = 'Mercedes'
print(temp_str+temp_str_2)
print(temp_str_2*2)

# Форматирование строк
brend = 'Volvo'
price = 1.5
car = 'Марка!: {} цена: {}'.format(brend, price)
print(car)
car = f'Марка!: {brend} цена: {price}'
print(car)

# Методы

print(temp_str.split())
cars = 'Volvo,Audi,Lada'
print(cars.split())
print(cars.split(','))

#М Методы форматирования строк

print(cars.upper())
print(cars.title())
print(cars.lower())

# Замена подстроки в строке

email_adress = 'eMail: _mail_'
email = 'my_email@gmail.com'
print(email_adress.replace('_mail_',email))