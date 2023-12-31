# --- Set Наборы ---

# !!!Набор это неупорядоченая последовательность элементов
# !!!Набор содержит ТОЛЬКО УНИКАЛЬНЫЕ элементы. Все дубликаты удаляются автоматически
# В наборах обычно сохраняют однотипные данные
# Элементы в наборах не имеют индексов. Запрос к элементу по индексу невозможен
# В наборы нельзя добавлять изменяемые элементы (списки, словари). Можно добавлять кортежи

my_set = set()  # создание нового пустого набора
post_ids = {151, 224, 762, 91, 77}
post_ids2 = {151, 226, 91}
post_ids3 = {151, 762}
my_fruits = {'apple', 'lime', 'banana'}

post_ids.add(225)  # Добалвение элемента в набор
# Метод обьединения наборов (одинаковы элементы не дублируются) или |
all_ids = post_ids.union(post_ids2)
# Метод показывающий пересечение наборов (одинаковые элементы) или &
common_ids = post_ids.intersection(post_ids2)
# Метод проверяющий включен ли один набор в другой (является ли он подмножеством). Возвращает True или False
res = post_ids3.issubset(post_ids)
# Метод проверяющий является ли выбраный набор супернабором для другого (малого) набора
res2 = post_ids.issuperset(post_ids3)
# Метод показывающий отличие в эелементах по сравн. с другим набором
post_ids.difference(post_ids2)
post_ids3.discard(151)  # Метод удаляющий элемент из набора (1)
post_ids3.remove(762)  # Метод удаляющий элемент из набора (2)
copied_set = post_ids2.copy()  # Метод копирующий и создающий новый набор

a = {1, 2, 3, 5}
b = {1, 2, 3, 4}
# Метод указывающий на наличие отличный элементов от другого набора
a.difference(b)  # (5)
# (4, 5) Метод указывающий отличные элементы с двух наборов
a.symmetric_difference(b)


# --- Practical Task ---
first_set = {12, 13, 25, 26, 30, 31}
first_set.add(33)

second_set = {12, 13, 27, 28, 31, 33}
second_set.discard(12)

interected_set = first_set.intersection(second_set)
set_to_list = list(interected_set)
print(set_to_list)
