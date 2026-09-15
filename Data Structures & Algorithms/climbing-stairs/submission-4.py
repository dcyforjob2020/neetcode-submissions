class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {0: 1, 1: 1}

        def dfs(x):
            if x < 0:
                return 0

            if x in mem:
                return mem[x]

            mem[x] = dfs(x - 1) + dfs(x - 2)

            return mem[x]

        dfs(n)

        return mem[n] 