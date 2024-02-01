def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for (numerator, denominator), val in zip(equations, values):
            graph[numerator][denominator] = val
            graph[denominator][numerator] = 1 / val
        
        def dfs(start, end, visited):
            if start == end:
                return 1.0
            
            visited.add(start)
            for n, v in graph[start].items():
                if n not in visited:
                    temp = dfs(n, end, visited)
                    if temp != -1.0:
                        return temp * v
            return -1.0
        
        results = []
        for numerator, denominator in queries:
            if numerator not in graph or denominator not in graph:
                results.append(-1.0)
            else:
                results.append(dfs(numerator, denominator, set()))
        
        return results
