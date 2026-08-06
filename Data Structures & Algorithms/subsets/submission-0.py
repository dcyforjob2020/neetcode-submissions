class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        current = []

        def dfs(i):
            if i >= n:
                res.append(current.copy())
                return

            current.append(nums[i])
            dfs(i + 1)
            current.pop()

            dfs(i + 1)

        dfs(0)

        return res