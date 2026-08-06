class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        current = []

        def dfs(i):
            if sum(current) > target:
                return

            if sum(current) == target:
                res.append(current.copy())

                return

            if i >= n:
                return

            current.append(nums[i])
            dfs(i)
            current.pop()

            dfs(i + 1)

        dfs(0)

        return res

