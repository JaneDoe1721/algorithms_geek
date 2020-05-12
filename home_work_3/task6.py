# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

result = [random.randint(0, 50) for _ in range(0, 20)]
print(result)


pos_min = float('inf')
pos_max = 0
for itm in result:

    if itm > pos_max:
        pos_max = itm
    elif itm < pos_min:
        pos_min = itm
a = result.index(pos_min)
b = result.index(pos_max)


if a < b:
    total = sum(result[a+1:b-1])
    print(f'Сумма: {total}, между {a} и {b} элементами')
    if total == 0:
        print(f'сумма: {result[b-1]}')
elif b < a:
    total = sum(result[b+1:a-1])
    print(f'Сумма: {total}, между {b} и {a} элементами')
    if total == 0:
        print(f'сумма: {result[a-1]}')