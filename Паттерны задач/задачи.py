def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return left


def mySqrt(x):
    if x < 2:
        return x
    left, right = 0, x
    while left <= 20:
        mid = (left + right) // 2
        square = mid * mid
        if square == x:
            return square
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
    return right


def missingNumber(nums):
    n = len(nums)
    total_sum = n *(n+1) // 2
    return total_sum - sum(nums)




