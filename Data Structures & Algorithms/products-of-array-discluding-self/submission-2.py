class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1]

        total = 1

        for i in range(len(nums) - 1):
            total *= nums[i]
            prefix.append(total)

        total = 1

        for i in range(len(nums) - 1, 0, -1):
            total *= nums[i]
            postfix.append(total)

        return [prefix[i] * postfix[len(nums) - 1 - i] for i in range(len(nums))]
