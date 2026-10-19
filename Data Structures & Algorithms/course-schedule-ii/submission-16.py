class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        needs = {}
        nextVisit = deque()
        canTravel = defaultdict(list)
        res = []
        for i in range(numCourses):
            needs[i] = 0
        for pair in prerequisites:
            needs[pair[0]] += 1
            canTravel[pair[1]].append(pair[0])
        for course in needs:
            if needs[course] == 0:
                nextVisit.append(course)
        

        while nextVisit:
            currCourse = nextVisit.popleft()
            res.append(currCourse)
            taken.add(currCourse)
            for course in canTravel[currCourse]:
                needs[course] -= 1
                if needs[course] == 0:
                    nextVisit.append(course)
        if len(res) != numCourses:
            return []
        return res