import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


def merge_sort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    temp = [0] * (right - left + 1)
    i = left
    j = mid + 1
    k = 0

    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    arr[left: right + 1] = temp[:]

arr = [5, 2, 4, 1, 7]

n = len(arr)
print(arr)

merge_sort(arr, 0, n - 1)
print(arr)
