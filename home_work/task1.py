# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
# а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'),
# программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.

while True:
    a = int(input('Введите превое число: \n'))
    b = int(input('Введите второе число: \n'))
    operator = input('Введите оператор: \n')

    if operator == '+' or operator == '-' or operator == '/' or operator == '*' or operator == '0':
        if operator == '0':
            print('Завершение программы')
            break
        elif operator == '+':
            print(a + b)
        elif operator == '-':
            print(a - b)
        elif operator == '/' and b == 0:
            print('Делить на ноль запрещенно')
        elif operator == '/':
            print(a / b)
        elif operator == '*':
            print(a * b)
    else:
        print('Неправильно введен оператор')
