import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


def solve(arr, n):
    s = sum(arr)
    leftsum = 0

    for i in range(n):
        if leftsum == s - leftsum - arr[i]:
            return i + 1
        leftsum += arr[i]

    return -1

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    res = solve(arr, n)
    print(res)
    