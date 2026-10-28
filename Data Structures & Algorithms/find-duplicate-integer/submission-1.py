class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        amount = [0] * (n + 1)

        for e in nums:
            amount[e] += 1

        res = 1

        for i in range(n + 1):
            if amount[res] < amount[i]:
                res = i

        return res