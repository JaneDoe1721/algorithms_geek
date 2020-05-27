# Закодируйте любую строку по алгоритму Хаффмана.
import heapq  # модуль для работы с мин. кучей из стандартной библиотеки Python
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):  # класс для ветвей дерева - внутренних узлов
    def walk(self, code, acc):
        # чтобы обойти дерево нам нужно:
        self.left.walk(code, acc + "0")  # пойти в левого потомка, добавив к префиксу "0"
        self.right.walk(code, acc + "1")  # затем пойти в правого потомка, добавив к префиксу "1"


class Leaf(namedtuple("Leaf", ["char"])):  # класс для листьев дерева, у него нет потомков, но есть значение символа
    def walk(self, code, acc):
        # потомков у листа нет, по этому для значения мы запишем построенный код для данного символа
        code[self.char] = acc or "0"  # если строка длиной 1 то acc = "", для этого случая установим значение acc = "0"


def huffman_encode(s):
    result = []
    for itm, value in Counter(
            s).items():  # построим очередь с помощью цикла, добавив счетчик, уникальный для всех листь
        result.append((value, len(result), Leaf(itm)))  # очередь будет представлена частотой символа, счетчиком и самим символом
    heapq.heapify(result)  # очередь с приоритетами
    count = len(result)
    while len(result) > 1:
        value1, _count1, left = heapq.heappop(result)  # вытащим элемент с минимальной частотой - левый узел
        value2, _count2, right = heapq.heappop(result)  # вытащим следующий элемент с минимальной частотой - правый узел
        # поместим в очередь новый элемент, у которого частота равна суме частот вытащенных элементов
        heapq.heappush(result, (value1 + value2, count, Node(left, right)))  # добавим новый внутренний узел у которого
        # потомки left и right соответственно
        count += 1
    code = {}
    if result:
        [(_value, _count, root)] = result  # в очереди 1 элемент, приоритет которого не важен, а сам элемент - корень дерева
        root.walk(code, "")  # обойдем дерева от корня и заполним словарь для получения кодирования Хаффмана
    return code


def main():
    line = input('Введите строку для кодирования:\n')
    code = huffman_encode(line)
    encoded = "".join(code[itm] for itm in line)  # отобразим закодированную версию, отобразив каждый символ
    # в соответствующий код и конкатенируем результат
    print(f'Количсетво символов :{len(code)}, Длинна закодированной строки: {len(encoded)}')
    for itm in sorted(code):  # обойдем символы в словаре в алфавитном порядке с помощью функции sorted()
        print(f"{itm}: {code[itm]}")
    print(f'Закодированная строка: \n{encoded}')


if __name__ == "__main__":
    main()


# def huffman_decode(encoded, code):  # функция декодирования исходной строки по кодам Хаффмана
#     sx = []
#     enc_ch = ""
#     for ch in encoded:  # обойдем закодированную строку по символам
#         enc_ch += ch  # добавим текущий символ к строке закодированного символа
#         for dec_ch in code:  # постараемся найти закодированный символ в словаре кодов
#             if code.get(dec_ch) == enc_ch:  # если закодированный символ найден,
#                 sx.append(dec_ch)  # добавим значение раскодированного символа к массиву раскодированной строки
#                 enc_ch = ""  # обнулим значение закодированного символа
#                 break
#     return "".join(sx)  # вернем значение раскодированной строки


#
# def test(n_iter=100):  # добавим тест для проверки алгоритма
#     import random
#     import string  # модуль для работы со строками, чтобы получить значения символов по их коду
#
#     # сгененрируем строку из ascii-символов
#     for itm in range(n_iter):  # тест включает краевые случаи с пустой строкой и строкой из 1 символа
#         length = random.randint(0, 32)  # сгеренируем код символа
#         s = "".join(
#             random.choice(string.ascii_letters) for _ in range(length))  # получим символ по коду и добавим к строке
#         code = huffman_encode(s)  # выполним кодирование строки
#         encoded = "".join(code[itm] for itm in s)  # получим закодированную строку
#         assert huffman_decode(encoded, code) == s  # раскодируем строку и сравним ее с исходной строкой


