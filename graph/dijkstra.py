import sys
import math
import heapq
from collections import defaultdict


try:
    sys.stdin = open(sys.path[0] + '\\input.txt', 'r')
    sys.stdout = open(sys.path[0] + '\\output.txt', 'w')
except FileNotFoundError:
    pass


def add_edge(x, y, wt):
    # Undirected graph
    graph[x].add((y, wt))
    graph[y].add((x, wt))

graph = defaultdict(set)

add_edge(0, 1, 4); 
add_edge(0, 7, 8); 
add_edge(1, 2, 8); 
add_edge(1, 7, 11); 
add_edge(2, 3, 7); 
add_edge(2, 8, 2); 
add_edge(2, 5, 4); 
add_edge(3, 4, 9); 
add_edge(3, 5, 14); 
add_edge(4, 5, 10); 
add_edge(5, 6, 2); 
add_edge(6, 7, 1); 
add_edge(6, 8, 6); 
add_edge(7, 8, 7); 

# Dijkstra's single source shortest path

v = 9
src = 0

pq = []
dist = [math.inf] * v
heapq.heapify(pq)

heapq.heappush(pq, (0, src))
dist[src] = 0

while pq:
    x = heapq.heappop(pq)[1]

    for i in graph[x]:
        y, wt = i
        if dist[y] > dist[x] + wt:
            dist[y] = dist[x] + wt
            heapq.heappush(pq, (dist[y], y))

for i in range(v):
    print(i, dist[i])
