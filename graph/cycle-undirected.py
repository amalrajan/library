import sys
import collections


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


def add_edge(x, y):
    graph[x].append(y)
    graph[y].append(x)

def dfs(v, par):
    global cycle_start, cycle_end

    visited[v] = True

    for u in graph[v]:
        if u == par:
            continue
        if visited[u]:
            cycle_end = v
            cycle_start = u
            return True

        parent[u] = v
        if dfs(u, parent[u]):
            return True

    return False

graph = collections.defaultdict(list)
n = 3

add_edge(0, 1)
add_edge(1, 2)
add_edge(2, 0)

visited = [False] * n
parent = [-1] * n

cycle_start = -1
cycle_end = -1

for v in range(n):
    if not visited[v] and dfs(v, parent[v]):
        break

if cycle_start == -1:
    print('Acyclic')
else:
    cycle = [cycle_start]
    v = cycle_end
    while v != cycle_start:
        if not 0 <= v < n:
            break
        cycle.append(v)
        v = parent[v]
    cycle.append(cycle_start)

    print(cycle)
