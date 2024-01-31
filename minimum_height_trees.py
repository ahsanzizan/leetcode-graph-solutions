from collections import deque, defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
    
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        # leaves = nodes with only one neighbor
        leaves = [node for node in graph if len(graph[node]) == 1]
        
        # remove leaves iteratively until 1 or 2 nodes left
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for l in leaves:
                neighbor = graph[l].pop()
                graph[neighbor].remove(l)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
