class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        current = []

        def dfs(i, total):
            if total > target:
                return

            if total == target:
                res.append(current.copy())

                return

            if i >= n:
                return

            current.append(nums[i])
            dfs(i, total + nums[i])
            current.pop()

            dfs(i + 1, total)

        dfs(0, 0)

        return res

