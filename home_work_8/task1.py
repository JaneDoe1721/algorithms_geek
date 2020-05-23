# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
# Сколько рукопожатий было?
#
# Примечание. Решите задачу при помощи построения графа.
# № 1 количество друзей это вершины, а количество ребер это рукопожатия

n = int(input('Введите количество друзей: \n'))
i = 0
graph = [[1 for _ in range(n)] for _ in range(n)]

while i < len(graph):
    for itm, value in enumerate(graph[i]):
        if itm == i:
            graph[i][itm] = 0

    i += 1

print(*graph, sep='\n')


def number_of_ribs(graph):
    result = 0

    current = 0
    while current < len(graph):

        for itm in graph[current]:

            if itm != 0:
                result += 1

        current += 1

    return f'Количсетво рукопожатий равно: {result}'


print(number_of_ribs(graph))
