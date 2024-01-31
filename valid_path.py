class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {i: [] for i in range(n)}
        
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        visited = set()
        return self.dfs(graph, visited, source, destination)

    def dfs(self, graph, visited, current, destination):
        if current == destination:
            return True
        
        visited.add(current)

        # Iterate through all neighbours
        for n in graph[current]:
            if n not in visited:
                # Bismillah exit clause nya bener
                if self.dfs(graph, visited, n, destination):
                    return True
        
        return False # No valid path in the current node
