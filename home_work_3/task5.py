# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
#
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.
import random

numbers = [random.randint(-20, -1) for _ in range(10)]
print(numbers)
negative_number = float('-inf')

for itm in numbers:

    if itm > negative_number:
        negative_number = itm

a = numbers.index(negative_number)
print(f'Максимальный отрицательный элемент: {negative_number}, позиция в массиве {a}')

