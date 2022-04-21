'''
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором
 все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
'''
import random
from collections import deque

def gen_graph(n_ver):
    '''
    Функция генерирует граф
    :param n_ver: принимает количество вершин
    :return: возвращает граф в виде списка смежности
    '''
    count = 0
    way =[]
    while count < n_ver:
        n_edge = random.randint(1, n_ver - 1) #сколько ребер будет
        set_vertex = {random.randint(0, n_ver - 1) for i in range(n_edge)} # Направление ребер
        if count in set_vertex: # проверяем, чтобы не в себя
            count += 0
        else:
            count += 1
            way.append(list(set_vertex))
    return way


def graph_dfs(g,start, finish):
    '''
    Функция обходит граф в глубину
    :param g: Примимает граф , также начальную и конечную вершину
    :return: Возвращает путь
    '''
    parents = [None for _ in range(len(g))]  # хранение Вершин родителей
    is_visit = [False for _ in range(len(g))]  # список вершин в которых были уже
    is_visit[start] = True  # вершина начала движения уже через нее не проходим
    deq = deque([start])


    pass

graph = gen_graph(5)
print(*graph, sep='\n')
s = int(input("Введите начальную вершину: "))
f = int(input("Введите конечную вершину: "))
graph_dfs(graph, s, f)

