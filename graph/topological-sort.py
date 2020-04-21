import sys
from collections import defaultdict


try:
    sys.stdin = open(sys.path[0] + '\\input.txt', 'r')
    sys.stdout = open(sys.path[0] + '\\output.txt', 'w')
except FileNotFoundError:
    pass


def dfs(u):
    visited[u] = True

    for i in graph[u]:
        if not visited[i]:
            dfs(i)
    
    stack.append(u)


v, e = list(map(int, input().split()))
graph = defaultdict(list)

for i in range(e):
    a, b = list(map(int, input().split()))
    graph[a].append(b)

visited = [False] * v
stack = []

for i in range(v):
    if not visited[i]:
        dfs(i)

print(stack[::-1])

d = {i: chr(i + 65) for i in range(v)}
for i in reversed(stack):
    print(d[i], end=' ')