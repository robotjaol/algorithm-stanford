## Maaf Python, malas CPP

def merge_and_count(arr, temp_arr, left, mid, right):
    i = left    # Indeks awal subarray kiri
    j = mid + 1 # Indeks awal subarray kanan
    k = left    # Indeks awal merged array
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)  # left > arr[j]
            j += 1
        k += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # duplicate arrays
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count

def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count

# file include
file_path = "multiplication-algorithm.txt"
with open(file_path, "r") as file:
    data = list(map(int, file.readlines()))

temp_arr = [0] * len(data)

num_inversions = merge_sort_and_count(data, temp_arr, 0, len(data) - 1)
num_inversions
