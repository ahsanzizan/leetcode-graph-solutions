class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.adjacency_list = [[] for _ in range(n)]
        for from_node, to_node, cost in edges:
            self.adjacency_list[from_node].append((to_node, cost))

    def addEdge(self, edge: List[int]) -> None:
        from_node, to_node, cost = edge
        self.adjacency_list[from_node].append((to_node, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        min_heap = [(0, node1)]
        visited = set()
        distances = [float('inf')] * len(self.adjacency_list)
        distances[node1] = 0

        while min_heap:
            current_distance, current_node = heapq.heappop(min_heap)
            if current_node == node2:
                return current_distance
            
            if current_node == visited:
                continue
            
            visited.add(current_node)

            for n, cost in self.adjacency_list[current_node]:
                if n not in visited:
                    new_distance = current_distance + cost
                    if new_distance < distances[n]:
                        distances[n] = new_distance
                        heapq.heappush(min_heap, (new_distance, n))
        return -1
