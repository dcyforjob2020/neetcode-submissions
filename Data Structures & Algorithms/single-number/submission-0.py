class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for e in nums:
            result = result ^ e

        return result