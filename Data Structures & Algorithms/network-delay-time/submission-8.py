from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for e in times:
            adjList[e[0]].append((e[1], e[2]))
        
        visited = set()
        def bfs(src):
            nextVisit = []
            minTime = 0
            heapq.heappush(nextVisit, (0, src))
            while nextVisit:
                time, node = heapq.heappop(nextVisit)
                if node in visited:
                    continue
                minTime = time
                visited.add(node)
                for nei, neiTime in adjList[node]:
                    heapq.heappush(nextVisit, (minTime + neiTime, nei))
            return minTime
        
        mTime = bfs(k)
        if len(visited) == n:
            return mTime
        return -1
            
            
