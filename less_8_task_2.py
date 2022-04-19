'''
2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список
 вершин, которые необходимо обойти.
'''
g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 7, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]

def dijkstra(graph, start):
    l = len(graph)
    is_visit = [False] * l
    cost = [float('inf')] * l
    parents = [-1] * l

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):
        is_visit[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visit[i]:
                if cost[i] > vertex + cost[start]:
                     cost[i] = vertex + cost[start]
                     parents[i] = start

        min_cost = float('inf')
        for i in range(l):
            if min_cost > cost[i] and not is_visit[i]:
                min_cost = cost[i]
                start = i
    return cost

s = int(input('От какой вершины идти: '))
print(dijkstra(g, s))
