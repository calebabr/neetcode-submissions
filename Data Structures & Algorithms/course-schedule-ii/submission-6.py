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
        taken = set()
        for i in range(numCourses):
            if needs[i] == 0:
                takeNow.append(i)
                taken.add(i) 
        
        while takeNow:
            curr = takeNow.pop()
            if curr not in taken:
                taken.add(curr)
            for course in canTake[curr]:
                needs[course] -= 1
                if needs[course] == 0:
                    taken.add(course)
        
        if len(taken) == numCourses:
            return list(taken)
        else:
            # print(taken)
            return []