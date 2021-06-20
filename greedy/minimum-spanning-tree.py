import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


class DSU:
    def __init__(self, n):
        self.arr = list(range(n))
        self.szarr = [1] * n

    def dsu_root(self, i):
        while self.arr[i] != i:
            i = self.arr[self.arr[i]]
        return i

    def dsu_find(self, a, b):
        return self.dsu_root(a) == self.dsu_root(b)

    def dsu_weighted_union(self, a, b):
        root_a = self.dsu_root(a)
        root_b = self.dsu_root(b)

        if self.szarr[root_a] < self.szarr[root_b]:
            self.arr[root_a] = self.arr[root_b]
            self.szarr[root_b] += self.szarr[root_a]
        else:
            self.arr[root_b] = self.arr[root_a]
            self.szarr[root_a] += self.szarr[root_b]


edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
edges.sort(key=lambda x: x[2])
print('Edges: ', edges)

res = []
vertices = 4
i, e = 0, 0
dsu = DSU(vertices)

while e < vertices - 1:
    u, v, w = edges[i]
    i += 1

    if not dsu.dsu_find(u, v):
        e += 1
        res.append((u, v, w))
        dsu.dsu_weighted_union(u, v)
    
min_cost = 0
for e in res:
    print(e)
    min_cost += e[2]

print('Minimum cost: ', min_cost)
