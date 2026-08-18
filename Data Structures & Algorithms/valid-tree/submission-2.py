class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for i in range(n)]
        visited = {}

        for u, v in edges:
            adj[v].append(u)
            adj[u].append(v)
        
        def dfs(node, parent):
            
            visited[node] = 1

            for v in adj[node]:
                if v == parent:
                    continue

                if visited.get(v, 0) == 1:
                    return True

                if dfs(v, node):
                    return True

            visited[node] = 2

            return False

        res = dfs(0, None)

        return not res if len(visited) == n else False
