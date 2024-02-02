def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = []

        def dfs(node, path):
            if node == n - 1:  # has reach the destination node, append the path
                paths.append(path)
                return
            for neighbor in graph[node]:
                dfs(neighbor, path + [neighbor])

        dfs(0, [0])
        return paths
