def eventualSafeNodes(graph: List[List[int]]) -> List[int]:
        def dfs(node):
            if colors[node] == 1:
                return False
            if colors[node] == 2:
                return True

            colors[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            colors[node] = 2
            return True

        n = len(graph)
        colors = [0] * n  # 0 is not visited, 1 is visiting, 2 is visited

        safe_nodes = []
        for i in range(n):
            if dfs(i):
                safe_nodes.append(i)
              
        return safe_nodes
