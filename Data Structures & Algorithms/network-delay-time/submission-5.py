class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for t in times:
            adjList[t[0]].append((t[1], t[2]))
        
        # visited set to check if we've visited all and to not revisit vertices
        # heap to get smallest weight
        # at every iteration of heap, pop smallest. If vertex hasnt been visited yet, we visit it. Add the time to minTime
        minTime = 0
        nextVisit = []
        visited = set()
        heapq.heappush(nextVisit, (0, k))
        while nextVisit:
            time, node = heapq.heappop(nextVisit)
            if node in visited:
                continue
            visited.add(node)
            minTime += time
            for nei, neiTime in adjList[node]:
                heapq.heappush(nextVisit, (neiTime, nei))
        
        if len(visited) != n:
            return -1
        return minTime
