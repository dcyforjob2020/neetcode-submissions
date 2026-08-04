class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        q = deque()

        res = 0

        while max_heap or q:
            res += 1

            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)

                if cnt:
                    q.append((res + n ,cnt))

            if q and q[0][0] == res:
                heapq.heappush(max_heap, q.popleft()[1])

        return res