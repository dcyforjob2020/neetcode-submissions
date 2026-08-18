class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        res = True

        adj = [[] for i in range(n)]
        visited = {}

        for u, v in edges:
            adj[v].append(u)
            adj[u].append(v)
        
        def dfs(node, parent):
            nonlocal res
            
            visited[node] = 1

            for v in adj[node]:
                if v == parent:
                    continue

                if visited.get(v, 0) == 1:
                    res = False
                    return

                dfs(v, node)

            visited[node] = 2

        dfs(0, None)

        return res if len(visited) == n else False
