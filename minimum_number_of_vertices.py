    def findSmallestSetOfVertices(n: int, edges: List[List[int]]) -> List[int]:
        incoming_count = [0] * n
        for e in edges:
            incoming_count[e[1]] += 1
        
        smallest_set = []
        for i in range(n):
            if incoming_count[i] == 0:
                smallest_set.append(i)
        
        return smallest_set
