# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
#
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque

numbers = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}
numbers_reversed = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
}

number1 = list(input('Введите первое шестнадцатеричное число:\n'))
number2 = list(input('Введите второе шестнадцатеричное число:\n'))


def sum_numbers(numb1, numb2):
    numb1 = deque(numb1)
    numb2 = deque(numb2)
    numb1.reverse()
    numb2.reverse()
    if len(numb1) > len(numb2):
        numb1.append('0' * (len(numb1) - len(numb2)))
    elif len(numb2) > len(numb1):
        numb1.append('0' * (len(numb2) - len(numb1)))

    sum = deque([])
    mind = 0
    for ind, itm in enumerate(numb1):
        result = numbers[itm] + numbers[numb2[ind]] + mind
        if result <= 16:
            mind = 0
        else:
            mind = result // 16
        current_result = result - 16 * mind
        result = numbers_reversed[current_result]
        sum.appendleft(result)
    return list(sum)


def mult_numb(x, y):
    result = deque()
    spam = deque([deque() for _ in range(len(y))])

    x, y = x.copy(), deque(y)

    for i in range(len(y)):
        m = numbers[y.pop()]

        for j in range(len(x) - 1, -1, -1):
            spam[i].appendleft(m * numbers[x[j]])

        for _ in range(i):
            spam[i].append(0)

    transfer = 0

    for _ in range(len(spam[-1])):
        res = transfer

        for i in range(len(spam)):
            if spam[i]:
                res += spam[i].pop()

        if res < 16:
            result.appendleft(numbers_reversed[res])

        else:
            result.appendleft(numbers_reversed[res % 16])
            transfer = res // 16

    if transfer:
            result.appendleft(numbers_reversed[transfer])

    return list(result)


print(f'Сумма чисел: {sum_numbers(number1, number2)}')
print(f"Произведение чисел: {mult_numb(number1, number2)}")
