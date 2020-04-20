import sys
import math
import heapq
from collections import defaultdict


try:
    sys.stdin = open(sys.path[0] + '\\input.txt', 'r')
    sys.stdout = open(sys.path[0] + '\\output.txt', 'w')
except FileNotFoundError:
    pass


v, e = list(map(int, input().split()))
s = int(input()) # Source vertex
graph = defaultdict(list)

for i in range(e):
    src, dest, cost = list(map(int, input().split()))
    graph[src].append((dest, cost))


# Dijkstra's single source shortest path
distance = [math.inf] * v
previous = [None] * v
visited = [False] * v

distance[s] = 0
visited[s] = True

pq = [*range(v)]
heapq.heapify(pq)

print(pq)

while pq:
    u = heapq.heappop(pq)
    visited[u] = True

    for i in graph[u]:
        if not visited[i[0]]:
            temp_dist = distance[u] + i[1]
            if temp_dist < distance[i[0]]:
                distance[i[0]] = temp_dist
                previous[i[0]] = u

print(distance)
print(previous)
