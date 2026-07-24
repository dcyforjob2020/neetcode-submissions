class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        re_stones = [-e for e in stones]

        heapq.heapify(re_stones)

        while len(re_stones) > 1:
            stone1 = heapq.heappop(re_stones)
            stone2 = heapq.heappop(re_stones)

            if stone1 != stone2:
                heapq.heappush(re_stones, stone1 - stone2)

        return -re_stones[0] if re_stones else 0
