class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remain = {}

        for i in range(len(nums)):
            num = nums[i]

            if num in remain:
                return [remain[num], i]

            remain[target - num] = i