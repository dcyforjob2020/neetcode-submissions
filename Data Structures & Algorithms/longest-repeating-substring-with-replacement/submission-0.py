class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0

        count = {}

        l = 0

        for r in range(len(s)):
            c = s[r]
            count[c] = count.get(c, 0) + 1

            if (r - l) + 1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            result = max(result, (r - l + 1))

        return result