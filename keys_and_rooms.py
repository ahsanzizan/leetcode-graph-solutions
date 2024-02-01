def canVisitAllRooms(rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()
        
        def dfs(room):
            visited.add(room)
            
            for key in rooms[room]:
                if key not in visited:
                    dfs(key)

        # Start searching from room 0
        dfs(0)
        return len(visited) == n
