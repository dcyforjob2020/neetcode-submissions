class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for x, y in points:
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(min_heap, (distance, [x, y]))
            print(x, y)
            print(distance, [x, y])

        return [point for distance, point in heapq.nsmallest(k, min_heap)]