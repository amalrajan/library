import sys; sys.stdin = open('input.txt', 'r'); sys.stdout = open('output.txt', 'w')


def sq_root(n):
    if n == 0 or n == 1:
        return n

    low = 0
    high = n
    res = -1

    while low <= high:
        mid = low + (high - low) // 2

        if mid * mid == n:
            return mid
        elif mid * mid < n:
            low = mid + 1
            res = mid
        else:
            high = mid - 1

    return res


n = int(input())
print(sq_root(n))
