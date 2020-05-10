# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

quantity = int(input('Введите колличество чисел: \n'))
numeral = int(input('Введите цифру которую надо найти: \n'))

total = ''
for itm in range(1, quantity + 1):
    number = int(input(f"Введите число {itm}:\n"))
    while number > 0:
        result = number % 10
        if result == numeral:
            total += str(result)
        number //= 10

print(f'Цифра {numeral} встречаеться:{len(total)} раз(a)')