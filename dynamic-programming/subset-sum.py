import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


def subset_sum_recurse(arr, n, summ):
    if summ == 0:
        return True
    
    if n < 0 or summ < 0:
        return False

    incl = subset_sum_recurse(arr, n - 1, summ - arr[n])
    excl = subset_sum_recurse(arr, n - 1, summ)

    return incl or excl


def subset_sum_memoized(arr, n, summ, memo={}):
    if summ == 0:
        return True

    if n < 0 or summ < 0:
        return False

    key = (n, summ)

    if key not in memo:
        incl = subset_sum_memoized(arr, n - 1, summ - arr[n], memo)
        excl = subset_sum_memoized(arr, n - 1, summ, memo)
        memo[key] = incl or excl

    return memo[key]


def subset_sum_dp(arr, n, summ):
    T = [[False] * (summ + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        T[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, summ + 1):
            if arr[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = T[i - 1][j] or T[i - 1][j - arr[i - 1]]
    
    return T[-1][-1]


arr = [7, 3, 2, 5, 8]
summ = 14

print(subset_sum_recurse(arr, len(arr) - 1, summ))
print(subset_sum_memoized(arr, len(arr) - 1, summ))
print(subset_sum_dp(arr, len(arr), summ))
