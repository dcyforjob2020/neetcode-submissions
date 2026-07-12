class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0

        l, r = 0, len(height) - 1
        max_l, max_r = 0, 0

        while l <= r:
            if max_l < max_r:
                result += max(0, min(max_l, max_r) - height[l])

                max_l = max(max_l, height[l])
                l += 1
            else:
                result += max(0, min(max_l, max_r) - height[r])

                max_r = max(max_r, height[r])
                r -= 1

        return result