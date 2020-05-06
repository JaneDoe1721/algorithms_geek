# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = input('Число а:\n')
b = input('Число b:\n')
c = input('Число c:\n')
a, b, c = int(a), int(b), int(c)

if a > b:
    if b > c:
        if c > a:
            print(f'a = {a}')
        elif c < a:
            print(f'b = {b}')
    elif a > c:
        print(f'c ={c}')
    else:
        print(f'a = {a}')
elif c > b:
    print(f'b = {b}')
elif c > a:
    print(f"c ={c}")
else:
    print(f'a = {a}')