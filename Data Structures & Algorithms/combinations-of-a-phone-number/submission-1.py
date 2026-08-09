class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        n = len(digits)

        def dfs(i, cur):
            if i >= n:
                if cur:
                    res.append(cur)

                return

            digit = int(digits[i])
            
            iteration = 3

            if digit == 7 or digit == 9:
                iteration = 4

            for j in range(iteration):
                prefix = (digit - 2) * 3

                if digit > 7:
                    prefix += 1

                dfs(i + 1, cur + chr(ord("a") + prefix + j))


        dfs(0, "")

        return res
