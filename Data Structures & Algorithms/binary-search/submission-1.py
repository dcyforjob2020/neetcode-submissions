class Solution:
    # time complexity: O(logn)
    # space complexity: O(1)
    def search(self, nums: List[int], target: int) -> int:
        # return -1 if nums is None
        if not nums:
            return -1

        # use left and right to keep the searching part
        l, r = 0, len(nums) - 1

        # while l <= r
        while l <= r:
            # get the mid
            mid = (l + r) // 2

            # check if the num[mid] equals to target 
            if nums[mid] == target:
                return mid
            # elif num[mid] bigger target search left part
            elif nums[mid] > target:
                r = mid - 1
            # else search right part
            else:
                l = mid + 1

        # return -1 since not get target
        return -1