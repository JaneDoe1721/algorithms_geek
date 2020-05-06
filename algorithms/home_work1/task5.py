# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

number = input('Введите номер буквы в английском алфавите:\n')

if number.isdigit():
    number = int(number)
    if number <= 26:
        print(f'{chr(number + 96)}')
    elif number >= 27:
        print('Столько букв в алфавите нет')
else:
    print('Введите номер')



