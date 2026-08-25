# def max_sum_subbarray(nums, k):
#     window_sum = sum(nums[:k])
#     max_sum = window_sum
#     for i in range(k, len(nums)):
#         window_sum += nums[i] - nums[i - k]
#         max_sum = max(max_sum, window_sum)
#     return max_sum
# print(max_sum_subbarray([2,1,5,1,3,2], 4))


