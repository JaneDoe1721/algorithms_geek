# Определить, какое число в массиве встречается чаще всего.
import random

result = [random.randint(0, 10) for _ in range(20)]
print(result)
number_score = 0
number = 0
for itm in result:

    if number_score < result.count(itm):
        number_score = result.count(itm)
        number = itm

print(f'число {number} встречается {number_score} раз(а)')