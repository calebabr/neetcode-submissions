class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        needs = {}
        nextVisit = deque()
        visited = set()
        canTake = defaultdict(list)
        res = []

        # Create adjacency list and populate needs
        for pair in prerequisites:
            needs[pair[0]] = 1 + needs.get(pair[0], 0)
            canTake[pair[1]].append(pair[0])

        # Iterate through numCourses to populate nextVisit
        for i in range(numCourses):
            if i not in needs or needs[i] == 0:
                nextVisit.append(i)

        # bfs while nextVisit
        while nextVisit:
            course = nextVisit.popleft()
            visited.add(course)
            res.append(course)
            for nextCourse in canTake[course]:
                needs[nextCourse] -= 1
                if needs[nextCourse] == 0:
                    nextVisit.append(nextCourse)
            
        # if len(visited) = numCourses, return res
        if len(visited) == numCourses:
            return res 
        # else []
        return []

