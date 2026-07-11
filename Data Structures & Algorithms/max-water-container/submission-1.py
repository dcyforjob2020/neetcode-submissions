class Solution:
    # time complexity: O(n)
    # space complexity: O(1)
    def maxArea(self, heights: List[int]) -> int:
        # result
        res = 0

        # two points
        left, right = 0, len(heights) - 1

        while left < right:
            # get the max
            res = max(res, min(heights[left], heights[right]) * (right - left))

            # if heights[left] > heights[right]
            # right -= 1
            if heights[left] > heights[right]:
                right -= 1
            # else
            # left += 1
            else:
                left += 1

        # return max
        return res