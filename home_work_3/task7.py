# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.
import random

result = [random.randint(1, 49) for _ in range(20)]
print(result)

min_number1 = float('inf')
min_number2 = float('inf')
for itm in result:

    if itm < min_number1:
        min_number1 = itm

a = result.index(min_number1)
b = result.pop(a)


for itm in result:

    if itm < min_number2:
        min_number2 = itm

c = result.insert(a, min_number1)

print(min_number1)
print(min_number2)
