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
        lst_sorted = []
        result = data.split(' ')
        for itm in result:
            total.append(hashlib.sha1(itm.encode('utf - 8')).hexdigest())
        total = sorted(total)
        for itm in range(len(total) - 1):
            if total[itm] == total[itm + 1]:
                total[itm] = 0
        for itm in total:
            if itm != 0:
                lst_sorted.append(itm)

        return lst_sorted

    else:
        new_len = len(data)

        if not new_len & 1:
            n = 4
            args = [iter(data)] * n
            long = zip(*args)
            container = [''.join(itm) for itm in long]
            total_lst = []
            finally_lst = []
            for itm in container:
                total_lst.append(hashlib.sha1(itm.encode('utf-8')).hexdigest())
            total_lst = sorted(total_lst)
            for itm in range(len(total_lst) - 1):
                if total_lst[itm] == total_lst[itm + 1]:
                    total_lst[itm] = 0

            for itm in total_lst:
                if itm != 0:
                    finally_lst.append(itm)
            return finally_lst
        if new_len & 1:
            n = 3
            args = [iter(data)] * n
            long = zip(*args)
            container = [''.join(itm) for itm in long]
            total_lst = []
            finally_lst = []
            for itm in container:
                total_lst.append(hashlib.sha1(itm.encode('utf-8')).hexdigest())
            total_lst = sorted(total_lst)
            for itm in range(len(total_lst) - 1):
                if total_lst[itm] == total_lst[itm + 1]:
                    total_lst[itm] = 0

            for itm in total_lst:
                if itm != 0:
                    finally_lst.append(itm)
            return finally_lst


dat = input('Введите строку: \n')
print(f'Количество разных подстрок в строке: {len(counter(dat))}')
print('Их хеш:')
print(*counter(dat), sep='\n')
