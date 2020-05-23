# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
#
# Примечания:
#
# a. граф должен храниться в виде списка смежности;
#
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
# № 3 Написать алгоритм поиска в глубину

from collections import deque
n = int(input('Введите количество вершин: \n'))


def generation_graph(n):
    i = 0
    graph = [[itm for itm in range(n)] for _ in range(n)]

    while i < len(graph):
        for itm, value in enumerate(graph[i]):
            if itm == i:
                graph[i].pop(itm)

        i += 1

    return graph


g = generation_graph(n)
print(*g, sep='\n')


def dfs(graph, start, finish):
    parent = [None for _ in range(len(graph))]  # если были в данной вершине
    is_visited = [False for _ in range(len(graph))]  # Если не были в данной вершине

    deq = deque([start])  # отсюда начинаем двигаться
    is_visited[start] = True

    while len(deq) > 0:

        current = deq.pop()

        if current == finish:
            break
        for i, vertex in enumerate(graph[current]):
            if vertex and not is_visited[i]:
                is_visited[i] = True
                parent[i] = current
                deq.appendleft(i)

    else:
        return f'Из вершины {start} нельзя попасть в вершину {finish}'

    cost = 0  # стоимость пути
    way = deque([finish])  # целевая вершина
    i = finish

    while parent[i] != start:
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]
    cost += 1
    way.appendleft(start)

    return f'кратчайший путь {list(way)}  длинною в {cost} условных единиц'


s = int(input('От какой вершины идти: '))
f = int(input('До какой вершины идти: '))
print(dfs(g, s, f))
