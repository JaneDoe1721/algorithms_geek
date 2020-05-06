# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
symbol1 = input('Введите первую букву:\n')
symbol2 = input('Введите вторую букву:\n')

if symbol1.isascii() and symbol2.isascii():
    result = ord(symbol2.lower()) - ord(symbol1.lower())
    print(f'Буква {symbol1} находится на:{ord(symbol1) - 96} месте')
    print(f'Буква {symbol2} находится на:{ord(symbol2) - 96} месте')
    print(f'{result - 1} букв находится между ними')
else:
    print('Введите английские буквы')
