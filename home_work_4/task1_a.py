# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

# ВЫВОД:
# Сложность алгоритмов (On) - Линейная сложность, время их работы приблизительно одинаковые, за исключением последнего
# алгоритма.В последнем алгоритме не удалось вызвать timeit из-за перебора вызова функций.
# Выбор за первым вариантом. Он самый простой в написании.
import random
import cProfile


def min_numb1(n):
    min_number1 = float('inf')
    min_number2 = float('inf')
    result = [random.randint(5, 20) for _ in range(n)]

    for num in result:
        if num < min_number1 and num < min_number2:
            min_number1 = num
        elif num < min_number2:
            min_number2 = num

    return f'Из массива {result}, \nДва наименьших числа: {min_number1}, {min_number2}'


# cProfile.run('min_numb1(20)')
# 125 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 20    0.000    0.000    0.000    0.000 random.py:174(randrange)
# 20    0.000    0.000    0.000    0.000 random.py:218(randint)
# 20    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
# 1    0.000    0.000    0.000    0.000 task1_a.py:10(<listcomp>)
# 1    0.000    0.000    0.000    0.000 task1_a.py:7(min_numb_1)
# Рукурсий нет и не будет

# python3 -m timeit -n 1000 -s "import task1_a" "task1_a.min_numb1(20)"
# 1000 loops, best of 5: 37 usec per loop

# python3 -m timeit -n 1000 -s "import task1_a" "task1_a.min_numb1(50)"
# 1000 loops, best of 5: 94.3 usec per loop

# python3 -m timeit -n 1000 -s "import task1_a" "task1_a.min_numb1(100)"
# 1000 loops, best of 5: 180 usec per loop
# Время вызова увеличивается в половину






def min_numb2(n):
    min_number1 = float('inf')
    min_number2 = float('inf')
    result = [random.randint(5, 20) for _ in range(n)]

    for itm in result:

        if itm < min_number1:
            min_number1 = itm

    a = result.index(min_number1)
    b = result.pop(a)

    for itm in result:

        if itm < min_number2:
            min_number2 = itm

    c = result.insert(a, min_number1)

    return f'Из массива {result}, \nДва минимальных числа:{min_number1}, {min_number2}'


# cProfile.run('min_numb2(20)')
# 124 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 20    0.000    0.000    0.000    0.000 random.py:174(randrange)
# 20    0.000    0.000    0.000    0.000 random.py:218(randint)
# 20    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
# 1    0.000    0.000    0.000    0.000 task1_a.py:43(min_numb2)
# Рекурсий тоже нет, колличество вызовов также как и в первой

# python3 -m timeit -n 1000 -s "import task1_a" "task1_a.min_numb2(20)"
# 1000 loops, best of 5: 39.4 usec per loop

# python3 -m timeit -n 1000 -s "import task1_a" "task1_a.min_numb2(50)"
# 1000 loops, best of 5: 88.4 usec per loop

# python3 -m timeit -n 1000 -s "import task1_a" "task1_a.min_numb2(100)"
# 1000 loops, best of 5: 187 usec per loop
# ВРемя вызова так же как и предидущий вариант




def min_numb_3(n):
    min_number1 = float('inf')
    min_number2 = float('inf')
    result = [random.randint(5, 20) for _ in range(n)]

    for itm in result:

        if min_number1 > itm and itm < min_number2:
            min_number1 = itm
        elif itm < min_number2:
            min_number2 = itm

    if min_number1 == 5 and min_number2 == 5:
        return min_number1, min_number2

    return min_numb_3(n - 1)

# cProfile.run('min_numb_3(20)')
# 213 function calls (212 primitive calls) in 0.000 seconds
# 1    0.000    0.000    0.001    0.001 <string>:1(<module>)
# 144    0.000    0.000    0.000    0.000 random.py:174(randrange)
# 144    0.000    0.000    0.000    0.000 random.py:218(randint)
# 144    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
# 9/1    0.000    0.000    0.001    0.001 task1_a.py:51(min_numb)
# Колличество рекурсий 9

# cProfile.run('min_numb_3(30)')
# 1250 function calls (1242 primitive calls) in 0.001 seconds
# 1    0.000    0.000    0.001    0.001 <string>:1(<module>)
# 234    0.000    0.000    0.001    0.000 random.py:174(randrange)
# 234    0.000    0.000    0.001    0.000 random.py:218(randint)
# 234    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
# 9/1    0.000    0.000    0.001    0.001 task1_a.py:51(min_numb)
# Колличество рекурсий 9, колличество вызова функций увеличино

# cProfile.run('min_numb_3(50)')
# 524 function calls (523 primitive calls) in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 99    0.000    0.000    0.000    0.000 random.py:174(randrange)
# 99    0.000    0.000    0.000    0.000 random.py:218(randint)
# 99    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
# 2/1    0.000    0.000    0.000    0.000 task1_a.py:51(min_numb)
# Колличество рекурсий 2, Колличество вызова функций уменьшено

# Timeit вызвать не получилось, слишком большое коллчисетво вызовов
