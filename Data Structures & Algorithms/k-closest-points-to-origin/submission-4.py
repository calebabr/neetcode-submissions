class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        kClosest = []
        for p in points:
            dist = -1 * math.sqrt((p[0]) ** 2 + (p[1]) ** 2)
            heapq.heappush(kClosest, (dist, p))
            while len(kClosest) > k:
                heapq.heappop(kClosest)
        
        res = []
        while kClosest:
            _, p = heapq.heappop(kClosest)
            res.append([p[0], p[1]])
        
        return res