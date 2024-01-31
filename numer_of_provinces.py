def findCircleNum(isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces_count = 0

        def dfs(city):
            visited.add(city)
            # n for neighbor, c for city
            for n, c in enumerate(isConnected[city]):
                if c and n not in visited:
                    dfs(n)

        for city in range(n):
            if city not in visited:
                dfs(city)
                provinces_count += 1
        
        return provinces_count
