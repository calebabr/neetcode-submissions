class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        minTime = 0

        for t in times:
            adjList[t[0]].append((t[1], t[2]))
        
        nextVisit = []
        visited = set()
        heapq.heappush(nextVisit, (0, k))
        while nextVisit:
            time, node = heapq.heappop(nextVisit)
            if node in visited:
                continue
            minTime = time
            visited.add(node)
            for nei, time in adjList[node]:
                heapq.heappush(nextVisit, (time + minTime, nei))
        
        if len(visited) != n:
            return -1
        return minTime

         
