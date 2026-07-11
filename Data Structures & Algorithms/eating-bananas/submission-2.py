class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        
        while l <= r:
            # bananas-per-hour eating speed
            mid = l + (r - l) // 2
            # finish eating time
            time = 0
            
            # calculate the time
            for pile in piles:
                time += math.ceil(float(pile) / mid)
            
            # eat too fast 
            if time <= h:
                r = mid - 1
            # eat too slow eat
            else: 
                l = mid + 1
                
        return l