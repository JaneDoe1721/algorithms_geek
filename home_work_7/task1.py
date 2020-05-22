# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
#
# Примечания:
#
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
#
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
import random


def bubble_sorting(array):
    n = 1
    while n < size:
        buffy = False
        for i in range(size - n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                buffy = True

        if buffy == False:
            break

        n += 1


size = 10
array = [random.randint(-100, 99) for _ in range(size)]
print(array)
bubble_sorting(array)
print(array)
