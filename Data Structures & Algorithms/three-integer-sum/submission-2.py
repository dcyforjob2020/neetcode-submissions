class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res
        res = []
        duplicate = set()
        nums_len = len(nums)
        target = 0

        # sort nums
        nums.sort()

        # loop through nums
        for i in range(nums_len - 2):
            # left, right
            left, right = i + 1, nums_len - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # if total == target
                # res.append
                if total == target:
                    if (nums[i], nums[left], nums[right]) not in duplicate:
                        res.append([nums[i], nums[left], nums[right]])
                        duplicate.add((nums[i], nums[left], nums[right]))
                    left += 1
                # elif total > target
                # right - 1
                elif total > target:
                    right -= 1
                # elif total < target
                # left + 1
                else:
                    left += 1

        # return res
        return res