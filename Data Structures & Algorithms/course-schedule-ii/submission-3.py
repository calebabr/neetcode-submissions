class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        canTake = defaultdict(list)
        needs = {}
        for pair in prerequisites:
            canTake[pair[1]].append(pair[0])
            needs[pair[0]] = 1 + needs.get(pair[0], 0)
        for i in range(numCourses):
            if i not in needs:
                needs[i] = 0
        takeNow = []
        taken = []
        for i in range(numCourses):
            if needs[i] == 0:
                takeNow.append(i)
                # needs[i] = 0   
        while takeNow:
            curr = takeNow.pop()
            taken.append(curr)
            for course in canTake[curr]:
                needs[course] -= 1
                if needs[course] == 0:
                    taken.append(course)
        
        if len(taken) == numCourses:
            return taken
        else:
            print(taken)
            return []