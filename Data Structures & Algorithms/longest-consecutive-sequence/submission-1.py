class Solution:
    # time complexity: O(n)
    # space complexity: O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        # map
        union = defaultdict(int)
        longest = 0

        # loop through nums
        for num in nums:
            if union[num] == 0:
                union[num] = union[num - 1] + union[num + 1] + 1
                union[num - union[num - 1]] = union[num]
                union[num + union[num + 1]] = union[num]

                longest = max(union[num], longest)

        return longest