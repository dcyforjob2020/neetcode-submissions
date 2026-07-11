class Solution:
    # time complexity: O(logn)
    # space complexity: O(n)
    def search(self, nums: List[int], target: int) -> int:
        # find dispatch point
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1

        dispatch_point = r

        # sort nums
        sorted_nums = nums[dispatch_point:] + nums[:dispatch_point]

        # binary search
        l, r = 0, len(sorted_nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if sorted_nums[mid] == target:
                return (mid + dispatch_point) % len(sorted_nums)

            if sorted_nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1
