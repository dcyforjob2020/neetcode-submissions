from _heapq import heapify
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        max_heap = [(-nums[i], i) for i in range(k)]

        heapq.heapify(max_heap)

        for i in range(k - 1, len(nums)):
            heapq.heappush(max_heap, (-nums[i], i))

            while max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)

            res.append(-max_heap[0][0])

        return res