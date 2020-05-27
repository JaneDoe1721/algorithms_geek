# Закодируйте любую строку по алгоритму Хаффмана.

import heapq
from collections import Counter
from collections import namedtuple


class Unit(namedtuple("Unit", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Sheet(namedtuple("Sheet", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman(s):
    result = []
    for itm, value in Counter(
            s).items():
        result.append((value, len(result), Sheet(itm)))
    heapq.heapify(result)
    count = len(result)
    while len(result) > 1:
        value1, _count1, left = heapq.heappop(result)
        value2, _count2, right = heapq.heappop(result)
        heapq.heappush(result, (value1 + value2, count, Unit(left, right)))
        count += 1
    code = {}
    if result:
        [(_value, _count, root)] = result
        root.walk(code, "")
    return code


def main():
    line = input('Введите строку для кодирования:\n')
    code = huffman(line)
    encoded = "".join(code[itm] for itm in line)
    print(f'Количсетво символов :{len(code)}, Длинна закодированной строки: {len(encoded)}')
    for itm in sorted(code):
        print(f"{itm}: {code[itm]}")
    return f'Закодированная строка: \n{encoded}'


m = main()
print(m)



