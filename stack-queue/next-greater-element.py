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
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        
        if not stack:
            res[i] = -1
        else:
            res[i] = stack[-1]
        
        stack.append(arr[i])
    
    print(*res)
