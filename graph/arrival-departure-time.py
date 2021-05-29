import sys
import collections

try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


def DFS(graph, v, discovered, arrival, departure, time):
    time += 1
    arrival[v] = time
    discovered[v] = True

    for i in graph[v]:
        if not discovered[i]:
            time = DFS(graph, i, discovered, arrival, departure, time)
    
    time += 1
    departure[v] = time

    return time


graph = collections.defaultdict(list)
edges = [(0, 1), (0, 2), (2, 3), (2, 4), (3, 1), (3, 5), (4, 5), (6, 7)]
N = 8

for x, y in edges:
    graph[x].append(y)

arrival = [None] * N
departure = [None] * N
discovered = [False] * N

time = -1

for i in range(N):
    if not discovered[i]:
        time = DFS(graph, i, discovered, arrival, departure, time)

for i in range(N):
    print('Vertex {}: {} {}'.format(i, arrival[i], departure[i]))
