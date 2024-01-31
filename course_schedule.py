def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for c, prereq in prerequisites:
            graph[prereq].append(c)
            indegree[c] += 1
        
        # Queue with courses having no prereqeusites
        q = [c for c in range(numCourses) if indegree[c] == 0]
        finished = 0

        while q:
            current = q.pop(0)
            finished += 1
            for n in graph[current]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
        
        return finished == numCourses
