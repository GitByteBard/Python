'''
РАБОТА СО СПИСКАМИ

customers = ['Bob', 'John', 'Sian']

removed_el = customers.pop(0)  # присвоение удаленного значения переменной
print(customers)
print(removed_el)


index = [251, 574, 10, 1]  # сортировка списка
index.sort(reverse=False)
print(index)

greeting = 'Hello frm Python'
greet_letters = list(greeting)  # преобразование строки в список
print(greet_letters)


ratings = [2.3, 3, 4, 7, 8]

print(max(ratings))  # манипуляции со списком
print(sum(ratings))
print(sum(ratings) / len(ratings))
all_numbers = index + ratings  # обьединение списков
print(all_numbers)


# cсоздание копии списка. копирование метод Слайс(Вариант 1)
copied_ratings = ratings[:]
copied_ratings.pop(0)
copied_ratings.append('228')  # добавления значения в список
print(ratings)
print(copied_ratings)


copied_ratings2 = ratings.copy()  # использование метода Copy
copied_ratings2.append('188')
print(id(ratings) == id(copied_ratings2))  # проверка на сходство

# практика

nums = [10, 50, 0, 5, 100]
nums.insert(2, -5)  # метод добавления в список
# nums.clear() очищает список
# nums.extend('abc') добавление в списк элементов
other_nums = nums.copy()
other_nums.append(228)

print(nums)
print(len(other_nums))
# print(nums.count(5)) считает колво. указаных значений
'''

my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.2
}

# print(my_motorbike['price'])
my_motorbike['price'] = 7000  # изменение значений
my_motorbike['is_new'] = True  # добавление элементов
# del my_motorbike['engine_vol']  # удаление ключа из словаря

key_name = 'brand'  # присвоение ключа переменной
my_motorbike[key_name] = 'BMW'
# print(len(my_motorbike)) #получение колва клбчей в словаре
