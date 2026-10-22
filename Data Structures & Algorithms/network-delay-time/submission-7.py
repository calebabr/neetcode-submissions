class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Djkstra's algorithm
        # At every iteration, add the smallest weight that doesnt cause a cycle aka traverse to a vertex that has already been traversed to 
        # Keep track of minTime (time most recent vertex was added, weight of edge + time source was added)
        # adjlist of key source node, list of tuples of target node and weight
        adjList = defaultdict(list)
        for t in times:
            adjList[t[0]].append((t[1], t[2]))
        
        visited = set()

        def bfs(src):
            minTime = 0
            qVisit = []
            heapq.heappush(qVisit, (0, src))
            while qVisit:
                time, curr = heapq.heappop(qVisit)
                if curr in visited:
                    continue
                minTime = time
                visited.add(curr)
                
                for nei, nTime in adjList[curr]:
                    heapq.heappush(qVisit, (minTime + nTime, nei))
            
            return minTime
        
        mTime = bfs(k)

        if len(visited) != n:
            return -1
        return mTime
                
            

        