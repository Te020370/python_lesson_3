# Тип данных МНОЖЕСТВО (set)
 # Инициализация

temp_set = {} # dict
print(type(temp_set), temp_set)

temp_set = {} # set
print(type(temp_set), temp_set)

temp_list = [1,2,1,2,2,3,4,12,32]
temp_set = (set)(temp_list)
print(type(temp_set), temp_list)

# Обращения к элементам множества
print(1 in temp_set)
print(100 in temp_set)

for element in temp_set:
    print(element)

# Функции с множествами
# ----------
# Операции с множествами
 # Методы
my_set1 = ({1,2,3,4,5})
my_set2 = ({5,6,7,8,9})
my_set3 = my_set1.union(my_set2)
print(my_set3)
my_set4 = my_set1.difference(my_set2)
print(my_set4)