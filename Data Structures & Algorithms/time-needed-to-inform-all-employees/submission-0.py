class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # adjList {manager: [employee IDs]}
        adjList = defaultdict(list)
        for em, m in enumerate(manager):
            adjList[m].append(em)
        
        minTime = 0
        nextVisit = deque()
        nextVisit.append((0, headID))
        while nextVisit:
            time, ID = nextVisit.popleft()
            for empID in adjList[ID]:
                nextVisit.append((time + informTime[ID], empID))
                minTime = max(minTime, time + informTime[ID])
        
        return minTime