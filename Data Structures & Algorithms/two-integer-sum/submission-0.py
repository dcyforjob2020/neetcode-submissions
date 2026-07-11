class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sub_dict = {}

        for i in range(len(nums)):
            if nums[i] in sub_dict:
                return [sub_dict[nums[i]], i]

            sub_dict[target - nums[i]] = i
