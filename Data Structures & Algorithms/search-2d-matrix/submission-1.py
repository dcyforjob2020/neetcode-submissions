class Solution:
    # time complexity: O(log n * log m)
    # space complexity: O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # do binary search by the row's first element
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = l + (r - l) // 2
            mid_value = matrix[mid][0]

            if mid_value == target:
                return True
            if mid_value > target:
                r = mid - 1
            else:
                l = mid + 1
        
        # do binary search by the row
        row_l, row_r = 0, len(matrix[r]) - 1

        while row_l <= row_r:
            mid = row_l + (row_r - row_l) // 2
            mid_value = matrix[r][mid]

            if mid_value == target:
                return True
            if mid_value > target:
                row_r = mid - 1
            else:
                row_l = mid + 1

        return False