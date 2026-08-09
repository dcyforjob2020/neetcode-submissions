class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1

            return True

        n = len(s)

        cur = []

        def dfs(start, end):
            nonlocal s
            # print(cur)
            # print(s[start: end + 1])


            if isPalindrome(start, end):
                if end >= n - 1:
                    cur.append(s[start: end + 1])
                    res.append(cur.copy())
                    cur.pop()

                    return

                cur.append(s[start: end + 1])

                next_start = end + 1
                next_end = next_start

                while next_end <= n - 1:
                    dfs(next_start, next_end)
                    next_end += 1

                cur.pop()

        for i in range(n):
            dfs(0, i)

        return res