def findJudge(n, trust):
    trusted_by = [0] * (n + 1)
    trust_count = [0] * (n + 1)
    
    for i, j in trust:
        trust_count[i] += 1
        trusted_by[j] += 1
    
    for i in range(1, n + 1):
        if trust_count[i] == 0 and trusted_by[i] == n - 1:
            return i
    
    return -1
