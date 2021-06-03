import sys
import collections


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


def countPaths(graph, u, dest, visited=set()):
    global res

    visited.add(u)

    if u == dest:
        res += 1
    else:
        for nei in graph[u]:
            if nei not in visited:
                countPaths(graph, nei, dest, visited)

    visited.remove(u)



graph = collections.defaultdict(list)
edges = [('A', 'B'), ('A', 'E'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'E'), ('D', 'C')]
N = 5

for x, y in edges:
    graph[x].append(y)

src = 'A'
dest = 'E'

res = 0
countPaths(graph, src, dest)

print(res)
