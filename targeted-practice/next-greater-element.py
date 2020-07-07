import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    res = [0] * n
    s = []

    for i in range(n - 1, -1, -1):
        while s and s[-1] <= arr[i]:
            s.pop()
        
        if not s:
            res[i] = -1
        else:
            res[i] = s[-1]
        
        s.append(arr[i])
    
    print(*res)
