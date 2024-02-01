def loudAndRich(richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]

        for richer, poorer in richer:
            graph[poorer].append(richer)
        
        memo = [-1] * n

        def dfs(person):
            if memo[person] != -1:
                return memo[person]
            
            result = person
            for n in graph[person]:
                candidate = dfs(n)
                if quiet[candidate] < quiet[result]:
                    result = candidate
            memo[person] = result
            return result
        
        return [dfs(person) for person in range(n)]
