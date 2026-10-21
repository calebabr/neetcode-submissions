class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        minTime = 0
        nextVisit = []
        visited = set()

        for t in times:
            adjList[t[0]].append((t[1], t[2])) # target, time
        
        # Djkstra's algorithm: At every iteration, pop the min weight edge from the heap. If the edge doesnt create a cycle (vertex that it connects to hasnt been visited), add it and increment minTime by its weight
        
        heapq.heappush(nextVisit, (0, k))
        while nextVisit:
            time, curr = heapq.heappop(nextVisit)
            if curr in visited:
                continue
            visited.add(curr)
            minTime = time
            for (nei, t) in adjList[curr]:
                heapq.heappush(nextVisit, (minTime + t, nei))
        
        if len(visited) == n:
            return minTime
        return -1
            