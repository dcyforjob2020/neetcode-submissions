from _heapq import heapify
class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ""
        counts = {}

        for c in s:
            counts[c] = counts.get(c, 0) + 1

        max_h = [(-val, key) for key, val in counts.items()]
        heapq.heapify(max_h)

        last_c = ""

        while len(max_h) > 0:
            amount, cur_c = heapq.heappop(max_h)

            if cur_c == last_c:
                if len(max_h) == 0:
                    return ""
                else:
                    second_amount, second_c = heapq.heappop(max_h)
                    last_c = second_c
                    res += second_c
                    
                    heapq.heappush(max_h, (amount, cur_c))

                    if second_amount + 1 < 0:
                        heapq.heappush(max_h, (second_amount + 1, second_c))
            else:
                last_c = cur_c
                res += cur_c

                if amount + 1 < 0:
                    heapq.heappush(max_h, (amount + 1, cur_c))

        return res