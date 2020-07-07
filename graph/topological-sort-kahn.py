import sys
import heapq
from collections import defaultdict


try:
    sys.stdin = open(sys.path[0] + '\\input.txt', 'r')
    sys.stdout = open(sys.path[0] + '\\output.txt', 'w')
except FileNotFoundError:
    pass


v, e = list(map(int, input().split()))
adj = defaultdict(list)

for i in range(e):
    a, b = list(map(int, input().split()))
    adj[a].append(b)

res = []
visited = [False] * v
in_degree = [0] * v

for i in adj:
    for j in adj[i]:
        in_degree[j] += 1

pq = []
for i in range(v):
    if in_degree[i] == 0:
        pq.append(i)
        visited[i] = True

heapq.heapify(pq)

while pq:
    u = heapq.heappop(pq)
    res.append(u)

    for i in range(v):
        if i in adj[u] and not visited[i]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                heapq.heappush(pq, i)
                visited[i] = True

print(res)
