# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(5)]

for line in matrix:
    for itm in line:
        print(f'{itm:>4}', end='')
    print()

min_column = [float('inf')] * len(matrix[0])

for line in matrix:

    for i, item in enumerate(line):
        if min_column[i] > item:
            min_column[i] = item

print('\nМинимальные элементы в столбцах матрицы:')

number = 0

for s in min_column:
    print(f'{s:>4}', end='')

    if number < s:
        number = s

print(f'\n\nМаксимальный элемент среди минимальных: {number}')

