class Solution:
    # tc: O(nlogn)
    # sc: O(n)
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for stone in stones:
            heapq.heappush(max_heap, -stone)

        while len(max_heap) > 1:
            largest = -heapq.heappop(max_heap)
            second_largest = -heapq.heappop(max_heap)

            new_weight = largest - second_largest

            heapq.heappush(max_heap, -new_weight)

        return -heapq.heappop(max_heap)

