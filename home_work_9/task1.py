# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
#
# Примечания:
#
# * в сумму не включаем пустую строку и строку целиком;
#
# * без использования функций для вычисления хэша (hash(),
# sha1() или любой другой из модуля hashlib задача считается не решённой.

# №1 написать функцию которая на вход принимает строку анализирует
# ее и возвращает целое число(количество подстрок в данной строке)
import hashlib


def counter(data):
    if data.count(' ') > 0:
        total = []
        result = data.split(' ')
        for itm in result:
            total.append(hashlib.sha1(itm.encode('utf - 8')).hexdigest())
        total = set(sorted(total))
        return total

    else:
        new_len = len(data)

        if not new_len & 1:
            n = 4
            args = [iter(data)] * n
            long = zip(*args)
            container = [''.join(itm) for itm in long]
            total_lst = []
            for itm in container:
                total_lst.append(hashlib.sha1(itm.encode('utf-8')).hexdigest())
            total_lst = set(sorted(total_lst))
            return total_lst
        if new_len & 1:
            n = 3
            args = [iter(data)] * n
            long = zip(*args)
            container = [''.join(itm) for itm in long]
            total_lst = []
            for itm in container:
                total_lst.append(hashlib.sha1(itm.encode('utf-8')).hexdigest())
            total_lst = set(sorted(total_lst))
            return total_lst


dat = input('Введите строку: \n')
print(f'Количество разных подстрок в строке: {len(counter(dat))}')
print('Их хеш:')
print(*counter(dat), sep='\n')
