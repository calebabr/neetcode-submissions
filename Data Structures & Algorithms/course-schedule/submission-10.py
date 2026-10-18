class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        canTake = defaultdict(list)
        needs = {}
        taken = 0

        for i in range(numCourses):
            needs[i] = 0
            canTake[i] = []
        
        for pair in prerequisites:
            needs[pair[0]] += 1
            canTake[pair[1]].append(pair[0])
        
        takeNow = deque()
        for course in needs:
            if needs[course] == 0:
                takeNow.append(course)
                
            
        def bfs():
            t = 0
            while takeNow:
                currCourse = takeNow.popleft() # Process by taking it and decrementing 1 from all courses that need it
                t += 1
                for course in canTake[currCourse]:
                    needs[course] -= 1
                    if needs[course] == 0:
                        takeNow.append(course)
            return t
                    
        taken = bfs()

        return taken == numCourses