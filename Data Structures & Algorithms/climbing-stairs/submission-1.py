class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {0: 1, 1: 1}

        def climb(x):
            if x in dp:
                return dp[x]

            dp[x] = climb(x - 2) + climb(x - 1)

            return dp[x]

        return climb(n)

            