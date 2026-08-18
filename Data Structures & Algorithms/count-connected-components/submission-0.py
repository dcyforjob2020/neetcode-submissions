class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0

        visited = set()


        adj = [[] for i in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            visited.add(node)

            for v in adj[node]:
                if v in visited:
                    continue

                dfs(v)


        for i in range(n):
            if i in visited:
                continue

            res += 1
            dfs(i)

        return res
