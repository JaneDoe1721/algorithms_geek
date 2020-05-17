# 1. Пользователь вводит данные о количестве предприятий, их наименования и
# прибыль за четыре квартала для каждого предприятия. Программа должна определить
# среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.
from collections import namedtuple

Enterprise = namedtuple('Enterprise', 'name quarter_1 quarter_2 quarter_3 quarter_4 year')

enterprise_count = int(input('Введите количество предприятий для анализа: '))
enterprises = [0 for _ in range(enterprise_count)]
profit_sum = 0

for itm in range(enterprise_count):
    name = input(f'Введите название {itm + 1}-го предприятия: ')
    quarters = [float(j) for j in input('Введите через пробел прибыль в каждом квартале: ').split()]

    profit_year = 0
    for quarter in quarters:
        profit_year += quarter

    profit_sum += profit_year
    enterprises[itm] = Enterprise(name, *quarters, profit_year)


if enterprise_count == 1:
    print(f'Для анализа передано 1 предприятие: {enterprises[0].name}. Eго годовая прибыль: {enterprises[0].year}')

else:
    profit_average = profit_sum / enterprise_count

    less = []
    more = []

    for i in range(enterprise_count):

        if enterprises[i].year < profit_average:
            less.append(enterprises[i])

        elif enterprises[i].year > profit_average:
            more.append(enterprises[i])

    print(f'\nСредняя годовая прибыль по предприятиям: {profit_average: .2f}')

    print(f'Предприятия, чья прибыль меньше {profit_average: .2f}:')
    for ent in less:
        print(f'\tПредприятие "{ent.name}" с прибылью {ent.year: .2f}')

    print(f'\nПредприятия, чья прибыль больше {profit_average: .2f}:')
    for ent in more:
        print(f'\tПредприятие "{ent.name}" с прибылью {ent.year: .2f}')
