# По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
# проходящей через эти точки.

print("Введите Коордиты точки A(x1,y1): ")
x1 = input('x1=:\n')
y1 = input('y1=:\n')

print('Введите Координаты точки B(x2, y2): ')
x2 = input('x2=:\n')
y2 = input('y2=:\n')

k = (float(y1) - float(y2)) / (float(x1) - float(x2))
b = float(y2) - k * float(x2)

print('Уравнение прямой проходящие через эти точки: ')
print(f"y = {k}* x + {b}")
