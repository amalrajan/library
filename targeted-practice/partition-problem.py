import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


def partition(A, n, summ):
    T = [[False for x in range(summ + 1)] for y in range(n + 1)]

    for i in range(n + 1):
        T[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, summ + 1):
            if A[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = T[i - 1][j] or T[i - 1][j - A[i - 1]]

    return T[n][summ]

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)

    res = (total & 1 == 0) and partition(arr, n, total // 2)
    print('YES' if res else 'NO')
