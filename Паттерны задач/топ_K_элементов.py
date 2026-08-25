import heapq

def kth_largest(nums, k):
    # min-heap размером k
    heap = []
    for v in nums:
        heapq.heappush(heap, v)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

print(kth_largest([3,2,1,5,6,4], 2))
