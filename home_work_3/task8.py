# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

matrix = [[int(input('Введите число:\n')) for _ in range(3)] for _ in range(5)]

for i, item in enumerate(matrix):
    matrix[i].append(sum(matrix[i]))

for line in matrix:

    for itm in line:
        print(f'{itm:>4}', end='')
    print()
