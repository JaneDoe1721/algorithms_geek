# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
# которые необходимо обойти.
# № 2 до каждой вершины вы должны вернуть соответсвующий путь, для 0 вершины вы возвращаете 0,
# а для вершины 5 вы должны вернуть список 0 2 4 6 5.

graph = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 1],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length  # посещали мы вершину или нет
    cost = [float('inf')] * length  # стоимость пути до конкретной вершины
    parent = [-1] * length  # пока мы не знаем родителя там хранится -1, а как узнаем будем записывать номер вершины

    cost[start] = 0  # cтоимость пути
    min_cost = 0  # минимальная стоимость, будет показывать двигаемся мы по графу или уже нет

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:  # проверяем расстояние
                    cost[i] = vertex + cost[start]  # замена
                    parent[i] = start  # указываем родителя

        min_cost = float('inf')
        for i in range(length):  # пройдет по всем вершинам графа
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i  # значение из текущей вершины

    result = [[] for _ in range(length)]

    for itm in range(length):
        if is_visited[itm]:
            result[itm].append(itm)
            n = itm
            while parent[n] != -1:
                result[itm].append(parent[n])
                n = parent[n]

            result[itm].reverse()

    return f'{cost} \n{result}'


s = int(input('От какой вершины идти: '))
print(dijkstra(graph, s))
