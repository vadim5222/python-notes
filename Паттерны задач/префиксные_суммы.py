def range_sum(nums, i, j):
    P = []
    total = 0
    for v in nums:
        total += v
        P.append(total)
    return P[j] - (P[i-1] if i > 0 else 0)

nums = [1,2,3,4,5,6]
print(range_sum(nums, 2, 2))