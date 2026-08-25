def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        elif s > target:
            right -= 1
    return []

print(two_sum_sorted([1,2,3,4,5], 3))