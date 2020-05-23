# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
#
# Примечания:
#
# a. граф должен храниться в виде списка смежности;
#
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.


import random

n = int(input('Введите количество вершин: \n'))


def generation_graph(n):
    i = 0
    graph = [[itm for itm in range(random.randint(0, n))] for _ in range(n)]

    while i < len(graph):
        for itm, value in enumerate(graph[i]):
            if itm == i:
                graph[i].pop(itm)

        i += 1

    return graph


g = generation_graph(n)
print(*g, sep='\n')


def dfs(graph, start):
    path = []
    parent = [None for _ in range(len(graph))]  # если были в данной вершине
    is_visited = [False for _ in range(len(graph))]  # Если не были в данной вершине

    def dfs_1(vertex):
        is_visited[vertex] = True
        path.append(vertex)

        for itm in graph[vertex]:
            if not is_visited[itm]:
                parent[itm] = vertex
                dfs_1(itm)
                path.append(vertex)

        else:
            path.append(-vertex)

    dfs_1(start)

    return parent, path


s = int(input('От какой вершины идти: '))
print(dfs(g, s))
