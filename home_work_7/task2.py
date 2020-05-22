# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

size = 10
array = [random.uniform(0, 49) for _ in range(10)]
print(array)


def grouping(array):
    m = 1
    while m < len(array):
        j = 0
        while j + m < len(array):
            merge(j, m, m)
            j += m + m
        m += m
    return array


def merge(j, r, m):
    if j + r < len(array):
        if m == 1:
            if array[j] > array[j + r]:
                array[j], array[j + r] = array[j + r], array[j]
        else:
            m = m // 2
            merge(j, r, m)
            if j + r + m < len(array):
                merge(j + m, r, m)
            merge(j + m, r - m, m)
    return array


print(grouping(array))
