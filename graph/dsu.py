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


dsu = DSU(10)
print(dsu.arr)
dsu.dsu_weighted_union(2, 3)
print(dsu.arr)
dsu.dsu_weighted_union(0, 1)
print(dsu.arr)
print(dsu.szarr)
