import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


def matrix_mul(dims, i, j):
    if j <= i + 1:
        return 0

    mini = float('inf')

    for k in range(i + 1, j):
        cost = matrix_mul(dims, i, k) + matrix_mul(dims, k, j)
        cost += (dims[i] * dims[k] * dims[j])
        mini = min(mini, cost)
    
    return mini

def matrix_mul_memoized(dims, i, j, memo):
    if j <= i + 1:
        return 0

    mini = float('inf')
    key = (i, j)

    if key not in memo:
        for k in range(i + 1, j):
            cost = matrix_mul_memoized(dims, i, k, memo) + matrix_mul_memoized(dims, k, j, memo)
            cost += (dims[i] * dims[k] * dims[j])
            mini = min(cost, mini)
        memo[key] = mini
    
    return memo[key]

dims = [10, 30, 5, 60]
print(matrix_mul(dims, 0, len(dims) - 1))
print(matrix_mul_memoized(dims, 0, len(dims) - 1, {}))
