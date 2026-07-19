class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0

        count = {}

        l = 0

        max_f = 0

        for r in range(len(s)):
            c = s[r]
            count[c] = count.get(c, 0) + 1
            max_f = max(max_f, count[c])

            if (r - l) + 1 - max_f > k:
                count[s[l]] -= 1
                l += 1

            result = max(result, (r - l + 1))

        return result