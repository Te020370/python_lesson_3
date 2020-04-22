# Тип данных саисок (list) ------------------------
#-------------------------------------------------

# Инициализация(генераторы)
temp_list = [] # пустой список
print(type(temp_list))
temp_list = [1.2, 123, 'Volvo', [1,2,3]]

for el in temp_list:
    print(el, type(el))

# list

list_str = list ("Volvo")
print(list_str)

# Обращение к элиментам списка подсписки
for i in range(len(temp_list)):
    print(i, ':', temp_list[i])
for i in range(len(temp_list)):
    print(i, ':', temp_list[i:])
for i in range(len(temp_list)):
    print(i, ':', temp_list[:i])

# Функции со списками
print(len(temp_list))

# Операции со списками
print(temp_list+list_str)
print(temp_list*2)

# Методы
# Append

integer_list = []
for i in range(5):
    integer_list.append(i)
print(integer_list)
integer_list.append(100)
print(integer_list)

# Remove удаление первого по вхождению
integer_list.remove(100)
print(integer_list)

#  Удалению по индексу
del integer_list[4]
print(integer_list)
# Reverse

integer_list.reverse()
print(integer_list)

# sort
integer_list = [6, 9, 2, 5]
integer_list.sort()
print(integer_list)

# insert
integer_list.insert(2,100)
print(integer_list)

# Обработка списков (map, filter, reduce)
# map
integer_list = [9, 3, 6, 2, 4]
#map(function, list) ----> map -----> list(map)
new_integer_list = list(map(lambda x: x**2, integer_list))
print(new_integer_list)

# filter
integer_list = [9,3,6,2,4]
new_integer_list = list(filter(lambda x: x<5, integer_list))
print(new_integer_list)

# reduce

from functools import reduce
integer_list = [1,2,3,4]
sum = reduce(lambda x,y: x+y, integer_list)
product = reduce(lambda x,y: x*y, integer_list)
print(sum, product)

