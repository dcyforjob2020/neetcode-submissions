class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        n = len(nums)

        cur = []
        copy = nums.copy()

        def dfs(left):
            if not left:
                res.append(cur.copy())

                return

            for i in range(len(left)):
                val = left[i]
                cur.append(val)
                left.pop(i)
                dfs(left)
                cur.pop()
                left.insert(i, val)

        dfs(copy)

        return res