# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите колличество элементов: \n'))

number = 1
result = 0
for itm in range(n):
    result += number
    number /= -2

print(result)