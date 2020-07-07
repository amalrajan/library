import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


for tc in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    hmap = {}
    for i in range(n):
        if arr[i] in hmap:
            hmap[arr[i]].append(i)
        else:
            hmap[arr[i]] = [i]

    arr.sort()
    mini = n
    res = 0

    for i in range(n):
        mini = min(mini, hmap[arr[i]][0])
        res = max(res, hmap[arr[i]][-1] - mini)
    
    print(res)
