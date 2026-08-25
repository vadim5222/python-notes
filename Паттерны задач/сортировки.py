def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[i]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[i])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

arr = [64, 34, 25, 12, 22, 11, 90, 88]
merge_arr = merge_sort(arr)
print(merge_arr) 




def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        print(f'проход номер: {i + 1}')
        for j in range(0, n - i - 1):
            if arr[j] > arr[i + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            print(f'{arr}')

        if not swapped:
            print('массив отсортирован досрочный выход')
            break
    return arr

arr = [10, 9, 56, 24]
print(bubble_sort(arr))


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

arr = [64, 34, 12, 11]
print(quick_sort(arr))