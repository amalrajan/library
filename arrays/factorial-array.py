import math
import sys
sys.stdin = open(sys.path[0] + '\\input.txt', 'r')
sys.stdout = open(sys.path[0] + '\\output.txt', 'w')


def multiply(a, b):
    m, n = len(a), len(b)
    res = [0] * (m + n)

    for i in range(m - 1, -1, -1):
        carry = 0
        for j in range(n - 1, -1, -1):
            temp = res[i + j + 1] + (a[i] * b[j]) + carry
            res[i + j + 1] = temp % 10
            carry = temp // 10
        res[i] += carry

    i = 0
    while i < m + n and res[i] == 0:
        i += 1
    res = res[i:]
    return res if res else [0]


def add_one(arr):
    m = len(arr)
    carry = 1

    for i in range(m - 1, -1, -1):
        arr[i] += carry
        carry = arr[i] // 10
        arr[i] %= 10

    if carry:
        return [carry] + arr
    return arr


for tc in range(int(input())):
    n = int(input())
    n_copy = n
    arr = [1]
    res = [1]

    for i in range(n_copy - 1):
        arr = add_one(arr)
        res = multiply(arr, res)

    for i in res:
        print(i, end='')
    print(end='\n')

print(math.factorial(13))
