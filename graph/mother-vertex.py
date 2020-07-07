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


v, e = list(map(int, input().split()))

graph = defaultdict(set)
visited = [False] * v

for _ in range(e):
    x, y = list(map(int, input().split()))
    graph[x].add(y)


# Obtain the last finished vertex.

last_v = 0
for i in range(v):
    if not visited[i]:
        dfs(i)
        last_v = i


# Check if last_v is a mother vertex.

visited = [False] * v
dfs(last_v)

if False in visited:
    print(None)
else:
    print(last_v)