import sys; sys.stdin = open('input.txt', 'r'); sys.stdout = open('output.txt', 'w')


arr = list(map(float, input().split()))
low, high = list(map(int, input().split()))

n = len(arr)
arr.sort()
print(arr)

# Counting triplets less than 'high'
cnt1 = 0
for i in range(n - 2):
    j = i + 1
    k = n - 1
    while j < k:
        if arr[i] + arr[j] + arr[k] >= high:
            k -= 1
        else:
            cnt1 += (k - j)
            j += 1

# Couting triplets less than or equal to 'low'
cnt2 = 0
for i in range(n - 2):
    j = i + 1
    k = n - 1
    while j < k:
        if arr[i] + arr[j] + arr[k] > low:
            k -= 1
        else:
            cnt2 += (k - j)
            j += 1

print(1 if cnt1 - cnt2 else 0)
