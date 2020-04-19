import sys


try:
    sys.stdin = open(sys.path[0] + '\\input.txt', 'r')
    sys.stdout = open(sys.path[0] + '\\output.txt', 'w')
except FileNotFoundError:
    pass


def backtrack(prev, level):
    global cnt, res

    if level == 0:
        res.append(prev)
        cnt += 1
        return

    for i in arr:
        if prev[0] != i[0] and prev[1] != i[1] and prev[2] != i[2]:
            backtrack(i, level - 1)


cnt = 0
res = []
arr = [
    'ABA',
    'ACA',
    'BCB',
    'BAB',
    'CAC',
    'CBC',
    'ABC',
    'BCA',
    'CAB',
    'CBA',
    'ACB',
    'BAC'
]

level = 4

for i in arr:
    backtrack(i, level)

print(cnt)
