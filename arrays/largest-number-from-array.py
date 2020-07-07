import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    maxlen = 1 + len(str(max(arr)))

    for i in range(n):
        val = str(arr[i]) * maxlen
        arr[i] = (arr[i], val[:maxlen])

    arr.sort(key=lambda a: a[1], reverse=True)
    
    res = ''
    for i in arr:
        res += str(i[0])

    return res


for _ in range(int(input())):
    res = solve()
    print(res)

