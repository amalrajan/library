import sys
from collections import defaultdict


# try:
#     sys.stdin = open(sys.path[0] + '\\input.txt', 'r')
#     sys.stdout = open(sys.path[0] + '\\output.txt', 'w')
# except FileNotFoundError:
#     pass


def dsu_root(i):
    while arr[i] != i:
        i = arr[arr[i]]
    return i


def dsu_find(a, b):
    return dsu_root(a) == dsu_root(b)


def dsu_weighted_union(a, b):
    root_a = dsu_root(a)
    root_b = dsu_root(b)

    if szarr[root_a] > szarr[root_b]:
        arr[root_b] = arr[root_a]
        szarr[root_a] += szarr[root_b]
    else:
        arr[root_a] = arr[root_b]
        szarr[root_b] += szarr[root_a]


v, e = list(map(int, input().split()))
edges = []

for i in range(e):
    a, b, w = list(map(int, input().split()))
    edges.append((a, b, w))

edges.sort(key=lambda a: a[2])
arr = [*range(v)]
szarr = [1] * v

graph = defaultdict(list)
for (a, b, w) in edges:
    if dsu_find(a, b):
        continue

    dsu_weighted_union(a, b)
    graph[a].append((b, w))
    graph[b].append((a, w))

for i in graph:
    print(i, '-->', *graph[i])
