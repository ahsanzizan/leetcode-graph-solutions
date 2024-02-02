def minReorder(n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))
        
        def dfs(node, parent):
            change_count = 0
            for n, is_forward in graph[node]:
                if n != parent:
                    if is_forward:
                        # if the edge is from node to n
                        change_count += 1 + dfs(n, node)
                    else:
                        # if the edge is from n to node
                        change_count += dfs(n, node)
            
            return change_count
        
        return dfs(0, -1)
