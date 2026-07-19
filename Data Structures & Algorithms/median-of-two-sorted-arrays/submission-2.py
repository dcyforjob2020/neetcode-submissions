class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(B) < len(A):
            A, B = B, A

        total_len = len(A) + len(B)
        half_len = total_len // 2
        l, r = 0, len(A) - 1

        while True:
            A_mid = l + (r - l) // 2
            B_mid = half_len - A_mid - 2

            A_left = A[A_mid] if A_mid >= 0 else float("-inf")
            A_right = A[A_mid + 1] if A_mid + 1 < len(A) else float("inf")
            B_left = B[B_mid] if B_mid >= 0 else float("-inf")
            B_right = B[B_mid + 1] if B_mid + 1 < len(B) else float("inf")

            if A_left <= B_right and B_left <= A_right:
                if total_len % 2:
                    return min(A_right, B_right)
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2

            if A_left > B_right:
                r = A_mid - 1
            else:
                l = A_mid + 1
