class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr_s = [0 for _ in range(26)]
        arr_t = [0 for _ in range(26)]

        for c in s:
            arr_s[ord(c) - ord("a")] += 1

        for c in t:
            arr_t[ord(c) - ord("a")] += 1

        return arr_s == arr_t