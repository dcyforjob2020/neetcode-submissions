class Solution:
    # time complexity: O(n)
    # space complexity: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # left, right
        left, right = 0, len(numbers) - 1

        while 1:
            total = numbers[left] + numbers[right]
            # if left + right == target
            # return [left, right]
            if total == target:
                return [left + 1, right + 1]
            # elif left + right > target
            # right - 1
            if total > target:
                right -= 1
            # elif left + right < target
            # left + 1
            else:
                left += 1