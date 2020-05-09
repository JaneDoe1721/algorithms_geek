# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

n = 0
max_sum = 0
max_numbers = 0
while n < 5:
    numbers = int(input('Введите число:\n'))
    num = numbers
    result = 0
    while numbers > 0:
        result += numbers % 10
        numbers //= 10
    if result > max_sum:
        max_sum = result
        max_numbers = num

    n += 1

print(f'Число {max_numbers} имеет самую большую сумму чисел: {max_sum}')