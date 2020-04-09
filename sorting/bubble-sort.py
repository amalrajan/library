def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

arr = [1, 5, 2, 8, 0]
sorted_arr = bubble_sort(arr, len(arr))

print(sorted_arr)