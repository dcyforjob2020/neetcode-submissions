class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem = {-2: 0, -1: 0}
        n = len(cost)
        cost.append(0)


        def dp(x):
            if x in mem:
                return mem[x]

            mem[x] = cost[x] + min(dp(x - 1), dp(x - 2))

            return mem[x]

        return dp(n)
