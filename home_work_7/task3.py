# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках
# (сортировка слиянием также недопустима).

import random

size = 5
array = [random.randint(0, 20) for _ in range(2 * size + 1)]
print(array)


def median_search(lst, first, last):

    lst = lst.copy()
    ind = len(lst) // 2

    if first >= last:
        return lst[ind]

    pillar = lst[ind]
    i = first
    j = last

    while i <= j:

        while lst[i] < pillar:
            i += 1

        while lst[j] > pillar:
            j -= 1

        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1

    if ind < i:
        lst[ind] = median_search(lst, first, j)

    elif j < ind:
        lst[ind] = median_search(lst, i, last)

    return lst[ind]


median = median_search(array, 0, len(array) - 1)
print(f'Медиана: {median}')


