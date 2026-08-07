class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        cur = []

        def dfs(i, left, right):
            if i >= 2 * n:
                if left == right:
                    res.append("".join(cur))

                return

            if left <= n:
                cur.append("(")
                dfs(i + 1, left + 1, right)
                cur.pop()

            if right < left:
                cur.append(")")
                dfs(i + 1, left, right + 1)
                cur.pop()

        dfs(0, 0, 0)

        return res