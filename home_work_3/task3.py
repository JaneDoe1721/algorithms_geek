# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

result = [random.randint(0, 50) for _ in range(0, 20)]
print(result)
min_number = 50
pos_min = 0
pos_max = 0
max_number = 0
for num, itm in enumerate(result, 0):

    if itm > max_number:
        max_number = itm
        pos_max = num
    elif itm < min_number:
        min_number = itm
        pos_min = num

a = result.pop(pos_min)
result.insert(pos_min, max_number)
b = result.pop(pos_max)
result.insert(pos_max, min_number)


print(result)