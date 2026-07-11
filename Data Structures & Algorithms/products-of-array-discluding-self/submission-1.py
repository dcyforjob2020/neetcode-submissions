class Solution:
    # time complexity: O(n)
    # space complexity: O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = [1 for _ in range(len(nums) + 2)]
        res = [1 for _ in range(len(nums))]
        nums_len = len(nums)

        # do the prefix
        # nums = [1, 2, 4, 6]
        # prefix = [1, 1, 2, 8]
        prefix = 1
        for i in range(nums_len - 1):
            prefix = prefix * nums[i]
            res[i + 1] =  prefix
        # res = [1, 1, 2, 6]

        # do the suffix
        # nums = [1, 2, 3, 4]
        # suffix = [1, 4, 12, 24]
        suffix = 1
        for i in range(nums_len - 1, 0 ,-1):
            suffix = suffix * nums[i]
            res[i - 1] = res[i - 1] * suffix
        # suffix = [24, 12, 4, 1]

        return res