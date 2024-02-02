def maximalNetworkRank(n: int, roads: List[List[int]]) -> int:
        c = [[0] * n for _ in range(n)] # connectivity

        city_rank = [0] * n

        for r in roads:
            a, b = r
            c[a][b] = 1
            c[b][a] = 1
            city_rank[a] += 1
            city_rank[b] += 1

        max_rank = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = city_rank[i] + city_rank[j] - c[i][j]
                max_rank = max(rank, max_rank)
        
        return max_rank
