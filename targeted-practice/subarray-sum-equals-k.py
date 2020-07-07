import sys
from collections import defaultdict


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


def solve(arr, n, k):
    hmap = defaultdict(int)
    hmap[0] = 1
    pref = 0

    for i in range(n):
        pref += arr[i]

        if pref == k:
            return (1, i + 1)
        elif pref - k in hmap:
            return (hmap[pref - k] + 2, i + 1)
        hmap[pref] = i

    return (-1, )

for tc in range(int(input())):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    res = solve(arr, n, k)
    print(*res)
    