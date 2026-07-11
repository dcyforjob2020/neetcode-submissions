class Solution:
    # time complexity: O(logn)
    # space complexity: O(1)
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        # binary search the deflection point 
        while l <= r:
            mid = l + (r - l) // 2

            if nums[l] <= nums[mid] and nums[mid] <= nums[r]:
                r = mid - 1
            elif nums[l] >= nums[mid] and nums[mid] <= nums[r]:
                r = mid
            elif nums[l] <= nums[mid] and nums[mid] >= nums[r]:
                l = mid + 1
            
        return nums[l]