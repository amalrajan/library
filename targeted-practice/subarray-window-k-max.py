import sys
from collections import deque


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    q = deque()

    for i in range(k):
        while q and arr[i] >= arr[q[-1]]:
            q.pop()

        q.append(i)

    for i in range(k, n):
        print(arr[q[0]], end=' ')

        while q and q[0] <= i - k:
            q.popleft()

        while q and arr[i] >= arr[q[-1]]:
            q.pop()

        q.append(i)

    print(arr[q[0]])
    