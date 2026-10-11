class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        canTake = defaultdict(list)
        needs = {}
        for i in range(numCourses):
            needs[i] = 0
            canTake[i] = []
        for pair in prerequisites:
            needs[pair[0]] += 1
            canTake[pair[1]].append(pair[0])
        
        waiting = []
        for i in range(numCourses):
            if needs[i] == 0:
                waiting.append(i)
        
        def bfs():
            while waiting:
                curr = waiting.pop()
                for course in canTake[curr]:
                    needs[course] -= 1
                    if needs[course] == 0:
                        waiting.append(course)
        bfs()
        for i in range(numCourses):
            if needs[i] > 0:
                return False
        return True