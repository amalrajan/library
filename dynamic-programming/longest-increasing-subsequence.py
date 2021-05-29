import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


def LIS(arr, i, n, prev):
    if i == n:
        return 0

    excl = LIS(arr, i + 1, n, prev)
    incl = 0
    if arr[i] > prev:
        incl = 1 + LIS(arr, i + 1, n, arr[i])
    
    return max(incl, excl)


def LIS_DP(arr, n):
    L = [0] * n
    L[0] = 1

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and L[j] > L[i]:
                L[i] = L[j]
        L[i] += 1

    return max(L)


for tc in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    print(LIS(arr, 0, n, float('-inf')))
    print(LIS_DP(arr, n))
