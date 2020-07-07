import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


def knapsack(vals, weights, n, W):
    if W < 0:
        return float('-inf')

    if n < 0 or W == 0:
        return 0

    incl = vals[n] + knapsack(vals, weights, n - 1, W - weights[n])
    excl = knapsack(vals, weights, n - 1, W)

    return max(incl, excl)

def knapsack_memoized(vals, weights, n, W, memo={}):
    if W < 0:
        return float('-inf')

    if n < 0 or W == 0:
        return 0
    
    key = (n, W)

    if key not in memo:
        incl = vals[n] + knapsack_memoized(vals, weights, n - 1, W - weights[n], memo)
        excl = knapsack_memoized(vals, weights, n - 1, W, memo)
        memo[key] = max(incl, excl)
    
    return memo[key]

def knapsack_dp(vals, weights, n, W):
    T = [[0] * (W + 1) for _ in range(n + 1)]

    # i = 0 means 0

    for i in range(1, n + 1):
        for j in range(W + 1):
            if j - weights[i - 1] < 0:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = max(T[i - 1][j], vals[i - 1] + T[i - 1][j - weights[i - 1]])
        
    return T[-1][-1]

vals = [20, 5, 10, 40, 15, 25]
weights = [1, 2, 3, 8, 7, 4]
W = 10

print(knapsack(vals, weights, len(vals) - 1, W))
print(knapsack_memoized(vals, weights, len(vals) - 1, W, {}))
print(knapsack_dp(vals, weights, len(vals), W))
