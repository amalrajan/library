import sys
import math


try:
    sys.stdin = open(sys.path[0] + '\\input.txt', 'r')
    sys.stdout = open(sys.path[0] + '\\output.txt', 'w')
except FileNotFoundError:
    pass


def primality_naive(n):
    # O(n) linear
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def primality_logn(n):
    # O(log n) logarithmic
    if n <= 1:
        return False

    if n == 2:
        return True

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


print(primality_naive(10000))
print(primality_logn(3))