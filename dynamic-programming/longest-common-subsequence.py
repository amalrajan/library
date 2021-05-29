import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


def LCS(X, Y, m, n):
    if m == 0 or n == 0:
        return 0

    if X[m - 1] == Y[n - 1]:
        return 1 + LCS(X, Y, m - 1, n - 1)
    else:
        return max(LCS(X, Y, m - 1, n), LCS(X, Y, m, n - 1))

def LCS_memoized(X, Y, m, n, memo={}):
    if m == 0 or n == 0:
        return 0

    key = (m, n)

    if key not in memo:
        if X[m - 1] == Y[n - 1]:
            memo[key] = 1 + LCS(X, Y, m - 1, n - 1)
        else:
            memo[key] = max(LCS(X, Y, m - 1, n), LCS(X, Y, m, n - 1))

    return memo[key]

def LCS_DP(X, Y, m, n):
    T = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                T[i][j] = 1 + T[i - 1][j - 1]
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])

    return T[-1][-1]

X = "ABCBDAB"
Y = "BDCABA"

# print(LCS(X, Y, len(X), len(Y)))
# print(LCS_memoized(X, Y, len(X), len(Y)))
# print(LCS_DP(X, Y, len(X), len(Y)))
