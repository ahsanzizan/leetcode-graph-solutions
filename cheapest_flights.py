# WARNING: This solution exceeds the time limit for several test cases

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}
    for flight in flights:
        from_city, to_city, price = flight
        if from_city not in graph:
            graph[from_city] = []
        graph[from_city].append((to_city, price))

    # (price, city, stops)
    pq = [(0, src, 0)]

    while pq:
        price, city, stops = heapq.heappop(pq)

        if city == dst:
            return price

        if stops > k:
            continue

        if city in graph:
            for neighbor, neighbor_price in graph[city]:
                heapq.heappush(pq, (price + neighbor_price, neighbor, stops + 1))

    return -1
