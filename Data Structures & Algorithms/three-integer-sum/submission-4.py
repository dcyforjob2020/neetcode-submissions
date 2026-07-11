class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        result_set = set()

        nums.sort()

        n = len(nums)

        for i in range(n - 2):
            l, r = i + 1, n - 1

            while l < r:
                sum = nums[i] + nums[l] + nums[r]

                if sum == 0:
                    if (nums[i], nums[l], nums[r]) not in result_set:
                        result.append([nums[i], nums[l], nums[r]])
                        result_set.add((nums[i], nums[l], nums[r]))
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    l += 1

        return result