import collections
import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


def DFS(graph, u, discovered):
    discovered[u] = True

    for nei in graph[u]:
        if not discovered[nei]:
            DFS(graph, nei, discovered)


def findRoot(graph, N):
    discovered = [False] * N

    last_vertex = 0
    for i in range(N):
        if not discovered[i]:
            DFS(graph, i, discovered)
            last_vertex = i

    discovered[:] = [False] * N
    DFS(graph, last_vertex, discovered)

    for i in range(N):
        if not discovered[i]:
            return -1

    return last_vertex


edges = [(0, 1), (1, 2), ( 2, 3), ( 3, 0), ( 4, 3), ( 4, 5), ( 5, 0)]
N = 6

graph = collections.defaultdict(list)
for x, y in edges:
    graph[x].append(y)

root = findRoot(graph, N)

if root == -1:
    print('No mother vertex')
else:
    print(root)
