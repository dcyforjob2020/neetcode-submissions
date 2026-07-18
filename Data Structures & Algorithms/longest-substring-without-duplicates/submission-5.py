class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        longest_substring_dict = {}
        start = -1

        for i, c in enumerate(s):
            if c in longest_substring_dict:
                start = max(start, longest_substring_dict[c])


            longest_substring_dict[c] = i
            result = max(result, i - start)

        return result