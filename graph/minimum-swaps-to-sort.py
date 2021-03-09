import sys
import collections


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


arr = [4, 3, 2, 1]
n = len(arr)

for i in range(n):
    arr[i] = (i, arr[i])

arr.sort(key=lambda x: x[1])

visited = collections.defaultdict(bool)
res = 0

for i in range(n):
    if visited[i] or arr[i][0] == i:
        continue

    cycle_size = 0
    j = i

    while not visited[j]:
        visited[j] = True
        j = arr[j][0]
        cycle_size += 1

    if cycle_size > 0:
        res += (cycle_size - 1)

print(res)
