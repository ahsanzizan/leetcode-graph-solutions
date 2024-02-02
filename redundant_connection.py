def findRedundantConnection(edges: List[List[int]]) -> List[int]:
        def find(parent, i):
            if parent[i] == -1:
                return i
            return find(parent, parent[i])
        
        def union(parent, x, y):
            x_set = find(parent, x)
            y_set = find(parent, y)
            parent[x_set] = y_set
        
        n = len(edges)
        parent = [-1] * n

        for e in edges:
            x = find(parent, e[0] - 1)
            y = find(parent, e[1] - 1)

            if x == y:
                return e
            union(parent, x, y)
        
        return []
