def findCenter(edges: List[List[int]]) -> int:
        count = {}

        for u, v in edges:
            count[u] = count.get(u, 0) + 1
            count[v] = count.get(v, 0) + 1
        
        # I assume we can just do this to get the center
        return max(count, key=count.get)
