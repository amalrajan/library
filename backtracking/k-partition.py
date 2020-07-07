import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


def check_sum(sum_left):
    for i in sum_left:
        if i:
            return False
    return True


def subset_sum(nums, n, sum_left, arr, k):
    if check_sum(sum_left):
        return True
    
    if n < 0:
        return False

    res = False

    for i in range(k):
        if not res and (sum_left[i] - nums[i]) >= 0:
            arr[n] = i + 1
            sum_left[i] -= nums[n]
            res = subset_sum(nums, n - 1, sum_left, arr, k)
            sum_left[i] += nums[n]

    return res


def partition(nums, k):
    n = len(nums)

    if n < k:
        print("Not possible to partition")
        return

    total = sum(nums)
    arr = [None] * n
    sum_left = [total // k] * k
    
    res = (total % k == 0) and subset_sum(nums, n - 1, sum_left, arr, k)

    if not res:
        print("Partition not possible")
        return

    for i in range(k):
        print("Partition {i} is", [nums[j] for j in range(n) if arr[j] == i + 1])


nums = [7, 3, 5, 12, 2, 1, 5, 3, 8, 4, 6, 4]
k = 5

partition(nums, k)
