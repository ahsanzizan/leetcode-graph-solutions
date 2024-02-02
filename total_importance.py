def maximumImportance(n: int, roads: List[List[int]]) -> int:
        degrees = {}
        for r in roads:
            for c in r:
                degrees[c] = degrees.get(c, 0) + 1
        
        sorted_cities = sorted(degrees.keys(), key=lambda x: degrees[x], reverse=True)

        values = {}
        current_value = n
        for c in sorted_cities:
            values[c] = current_value
            current_value -= 1
        
        importance = 0
        for r in roads:
            importance += values[r[0]] + values[r[1]]
        
        return importance
