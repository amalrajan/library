import sys
import collections


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


def add_edge(x, y):
    graph[x].append(y)

def dfs(v):
    global cycle_start, cycle_end
    color[v] = 1

    for u in graph[v]:
        if color[u] == 0:
            parent[u] = v
            if dfs(u):
                return True
        elif color[u] == 1:
            cycle_start = v
            cycle_end = u
            
            return True
    
    color[v] = 2

    return False

graph = collections.defaultdict(list)
n = 4

add_edge(0, 1)
add_edge(0, 2)
add_edge(1, 2)
add_edge(2, 0)
add_edge(2, 3)
add_edge(3, 3)

color = [0] * n
parent = [-1] * n

cycle_start = -1

for v in range(n):
    if color[v] == 0 and dfs(v):
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

    cycle.reverse()

    print(cycle)
