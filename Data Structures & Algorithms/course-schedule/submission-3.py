class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        canTake = defaultdict(list)
        needs = {}
        for i in range(numCourses):
            needs[i] = 0
            canTake[i] = []
        
        for prereq in prerequisites:
            needs[prereq[0]] += 1
            canTake[prereq[1]].append(prereq[0])

        print(needs)
        print(canTake)
        waiting = []
        for i in range(numCourses):
            if needs[i] == 0:
                waiting.append(i)
        while waiting:
            curr = waiting.pop()
            for course in canTake[curr]:
                needs[course] -= 1
                if needs[course] == 0:
                    waiting.append(course)

        for i in range(numCourses):
            if needs[i] > 0:
                return False   
        return True