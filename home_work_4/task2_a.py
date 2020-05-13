# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Второй — без использования «Решета Эратосфена».

# ВЫВОД:
# Сложность алгоритмов сильно отличаются, время их работы приблизительно одинаковые.
import cProfile


def get_primes(n):
    count = 1
    start = 3
    end = n * 4

    sieve = [i for i in range(start, end) if i % 2 != 0]
    prime = [2]

    if n == 1:
        return 2

    while count < n:

        for i in range(len(sieve)):

            if sieve[i] != 0:
                count += 1

                if count == n:
                    return sieve[i]

                j = i + sieve[i]

                while j < len(sieve):
                    sieve[j] = 0
                    j += sieve[i]

        prime.extend([i for i in sieve if i != 0])

        start, end = end, end + 2 * n
        sieve = [i for i in range(start, end) if i % 2 != 0]

        for i in range(len(sieve)):

            for num in prime:

                if sieve[i] % num == 0:
                    sieve[i] = 0
                    break


# cProfile.run('get_prime(100)')
# 1    0.000    0.000    0.000    0.000 task2_a.py:31(get_prime)
# 1    0.000    0.000    0.000    0.000 task2_a.py :36(<listcomp>)
# 1    0.000    0.000    0.000    0.000 task2_a.py :58(<listcomp>)
# 1    0.000    0.000    0.000    0.000 task2_a.py :61(<listcomp>)

# Рекурсий нет

# python3 -m timeit -n 1000 -s "import task2_a" "task2_a.get_primes(10)"
# 1000 loops, best of 5: 9.41 usec per loop

# python3 -m timeit -n 1000 -s "import task2_a" "task2_a.get_primes(100)"
# 1000 loops, best of 5: 372 usec per loop

# python3 -m timeit -n 1000 -s "import task2_a" "task2_a.get_primes(500)"
# 1000 loops, best of 5: 9.72 msec per loop

# Предположительно, алгоритм сложности O(n**2). Увеличение количества чисел в 10 раз
# увеличивает время выполнения приблизительно в 100 раз


def search_prime(n):
    count = 1
    number = 1
    prime = [2]

    if n == 1:
        return 2

    while count != n:
        number += 2

        for num in prime:
            if number % num == 0:
                break
        else:
            count += 1
            prime.append(number)

    return number

# cProfile.run('search_prime(7)')
# 10 function calls in 0.000 seconds
# 1   0.000 0.000   0.000   0.000   task2_a.py: 72(search_prime)
# Рекурсий нет


# python3 -m timeit -n 1000 -s "import task2_a" "task2_a.search_prime(10)"
# 1000 loops, best of 5: 6.7 usec per loop

# python3 -m timeit -n 1000 -s "import task2_a" "task2_a.search_prime(100)"
# 1000 loops, best of 5: 354 usec per loop

# python3 -m timeit -n 1000 -s "import task2_a" "task2_a.search_prime(500)"
# 1000 loops, best of 5: 8.58 msec per loop

# Сложность близка к O(n**2)
# Скорость работы обоих алгоритмов на данных объемах данных практически одинакова.
