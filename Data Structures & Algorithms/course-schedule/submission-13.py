class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        canTake = defaultdict(list)
        needs = {}
        taken = 0

        for i in range(numCourses):
            needs[i] = 0
            canTake[i] = []
            
        for pair in prerequisites:
            canTake[pair[1]].append(pair[0])
            needs[pair[0]] += 1
        
        nextVisit = deque()
        for i in range(numCourses):
            if needs[i] == 0:
                nextVisit.append(i)
        
        def bfs():
            haveTaken = 0
            while nextVisit:
                currCourse = nextVisit.popleft()
                haveTaken += 1
                for course in canTake[currCourse]:
                    needs[course] -= 1
                    if needs[course] == 0:
                        nextVisit.append(course)
            return haveTaken
        
        taken = bfs()
        return taken == numCourses
            