class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_frequency = {}

        for c in s:
            s_frequency[c] = s_frequency.get(c, 0) + 1

        t_frequency = {}

        for c in t:
            t_frequency[c] = t_frequency.get(c, 0) + 1

        return s_frequency == t_frequency