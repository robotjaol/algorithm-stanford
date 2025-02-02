## Maaf Python, malas CPP

def quicksort_first_pivot(arr, left, right):
    if left >= right:
        return 0

    pivot = arr[left]
    i = left + 1

    for j in range(left + 1, right + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[left], arr[i - 1] = arr[i - 1], arr[left]

    count = (right - left) 
    count += quicksort_first_pivot(arr, left, i - 2)  # Subarray kiri
    count += quicksort_first_pivot(arr, i, right)  # Subarray kanan

    return count


def quicksort_last_pivot(arr, left, right):
    if left >= right:
        return 0

    arr[left], arr[right] = arr[right], arr[left]

    pivot = arr[left]
    i = left + 1

    for j in range(left + 1, right + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[left], arr[i - 1] = arr[i - 1], arr[left]

    count = (right - left)
    count += quicksort_last_pivot(arr, left, i - 2)  
    count += quicksort_last_pivot(arr, i, right)  

    return count


def median_of_three(arr, left, right):
    mid = left + (right - left) // 2
    first, middle, last = arr[left], arr[mid], arr[right]

    if (first <= middle <= last) or (last <= middle <= first):
        median_index = mid
    elif (middle <= first <= last) or (last <= first <= middle):
        median_index = left
    else:
        median_index = right

    return median_index


def quicksort_median_pivot(arr, left, right):
    if left >= right:
        return 0

    median_index = median_of_three(arr, left, right)
    arr[left], arr[median_index] = arr[median_index], arr[left]  # Swap

    pivot = arr[left]
    i = left + 1

    for j in range(left + 1, right + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[left], arr[i - 1] = arr[i - 1], arr[left]

    count = (right - left)
    count += quicksort_median_pivot(arr, left, i - 2)
    count += quicksort_median_pivot(arr, i, right)

    return count


# Read File
file_path = "quick-short.txt"
with open(file_path, "r") as file:
    data = list(map(int, file.readlines()))

# sum first pivot
arr_first = data[:]
comparisons_first = quicksort_first_pivot(arr_first, 0, len(arr_first) - 1)

# # sum last pivot
arr_last = data[:]
comparisons_last = quicksort_last_pivot(arr_last, 0, len(arr_last) - 1)

# sum median pivot
arr_median = data[:]
comparisons_median = quicksort_median_pivot(arr_median, 0, len(arr_median) - 1)

comparisons_first, comparisons_last, comparisons_median

print(comparisons_first)
print(comparisons_last)
print(comparisons_median)
