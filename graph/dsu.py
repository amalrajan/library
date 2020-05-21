class DSU:
    def __init__(self, n):
        self.arr = list(range(1, n + 1))
        self.szarr = [1] * n

    def dsu_root(i):
        while self.arr[i] != i:
            i = self.arr[self.arr[i]]
        return i


    def dsu_find(a, b):
        return dsu_root(a) == dsu_root(b)


    def dsu_weighted_union(a, b):
        root_a = dsu_root(a)
        root_b = dsu_root(b)

        if self.szarr[root_a] < self.szarr[root_b]:
            self.arr[root_a] = self.arr[root_b]
            self.szarr[root_b] += self.szarr[root_a]
        else:
            self.arr[root_b] = self.arr[root_a]
            self.szarr[root_a] += self.szarr[root_b]


dsu = DSU(10)
print(dsu.arr)
