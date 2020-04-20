def dsu_root(i):
    while arr[i] != i:
        i = arr[arr[i]]
    return i


def dsu_find(a, b):
    return dsu_root(a) == dsu_root(b)


def dsu_weighted_union(a, b):
    root_a = dsu_root(a)
    root_b = dsu_root(b)

    if szarr[root_a] < szarr[root_b]:
        arr[root_a] = arr[root_b]
        szarr[root_b] += szarr[root_a]
    else:
        arr[root_b] = arr[root_a]
        szarr[root_a] += szarr[root_b]


n = 10
arr = list(range(1, n + 1))
szarr = [1] * 10
