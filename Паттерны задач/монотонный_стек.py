def next_greater(nums):
    result = [-1] * len(nums)
    stack = []

    for i, v in enumerate(nums):
        # пока стек не пуст и текущий > элемента на вершине
        while stack and nums[stack[-1]] < v:
            idx = stack.pop()
            result[idx] = v
        stack.append(i)
    return result

print(next_greater([2,1,2,4,3]))