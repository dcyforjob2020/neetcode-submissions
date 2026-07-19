class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)

        s1_map = {}
        
        for c in s1:
            s1_map[c] = s1_map.get(c, 0) + 1
        
        while r <= len(s2):
            s2_map = {}
            
            for c in s2[l: r]:
                s2_map[c] = s2_map.get(c, 0) + 1
            
            if s1_map == s2_map:
                return True

            l += 1
            r += 1

        return False