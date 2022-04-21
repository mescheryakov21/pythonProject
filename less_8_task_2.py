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
    way = []

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):
        is_visit[start] = True
        way_spam = []
        for i, vertex in enumerate(graph[start]):
            # way_spam.clear()
            if vertex != 0 and not is_visit[i]:
                if cost[i] > vertex + cost[start]:
                     cost[i] = vertex + cost[start]
                     parents[i] = start
        #     way_spam.append(i)
        # way.extend(way_spam)

        min_cost = float('inf')
        for i in range(l):
            if min_cost > cost[i] and not is_visit[i]:
                min_cost = cost[i]
                start = i

        way.append(way_spam)
    return cost

s = int(input('От какой вершины идти: '))
print(dijkstra(g, s))
# print(way)
