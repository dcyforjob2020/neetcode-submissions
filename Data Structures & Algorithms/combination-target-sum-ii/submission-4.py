class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        n = len(candidates)
        candidates.sort()

        cur = []
        visited = set()

        def dfs(i, total):
            if total == target:
                res.append(cur.copy())

                return

            if i >= n or total > target:
                return

            cur.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            cur.pop()

            while i < n - 1 and candidates[i] == candidates[i + 1]:
                i += 1
                
            dfs(i + 1, total)

        dfs(0, 0)

        return res
