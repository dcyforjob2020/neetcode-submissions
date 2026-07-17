class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[r] > nums[mid]:
                r = mid
            else:
                l = mid + 1

        pivot = r

        l, r = 0, pivot - 1

        while l <= r:
            mid = l + (r - l) // 2

            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid

        l, r = pivot, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid

        return -1
            