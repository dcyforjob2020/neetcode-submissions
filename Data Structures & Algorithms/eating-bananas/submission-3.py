class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            mid = l + (r - l) // 2

            total = 0

            for p in piles:
                total += p // mid

                if p % mid != 0:
                    total += 1

            if total <= h:
                r = mid - 1
            else:
                l = mid + 1

        return l

