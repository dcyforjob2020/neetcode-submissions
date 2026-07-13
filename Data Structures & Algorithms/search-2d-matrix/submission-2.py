class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1

        start_row = r

        l, r = 0, len(matrix[start_row]) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if matrix[start_row][mid] == target:
                return True
            elif matrix[start_row][mid]< target:
                l = mid + 1
            else:
                r = mid - 1

        return False

