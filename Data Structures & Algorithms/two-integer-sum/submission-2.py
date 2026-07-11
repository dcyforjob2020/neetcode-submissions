class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        less_map = {}

        for i in range(len(nums)):
            if nums[i] in less_map:
                return [less_map[nums[i]], i]

            less_map[target - nums[i]] = i