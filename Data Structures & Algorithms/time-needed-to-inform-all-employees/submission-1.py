class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjList = defaultdict(list)
        minTime = 0
        nextVisit = deque() # deque of time told, employee
        nextVisit.append((0, headID))

        for emp, man in enumerate(manager):
            adjList[man].append(emp)
        
        while nextVisit:
            time, man = nextVisit.popleft()
            for emp in adjList[man]:
                nextVisit.append((time + informTime[man], emp))
                minTime = max(minTime, time + informTime[man])
        
        return minTime  
