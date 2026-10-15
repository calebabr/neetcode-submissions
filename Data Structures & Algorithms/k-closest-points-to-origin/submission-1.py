class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        kClosest = []
        # heapq.heapify(kClosest)
        for p in points:
            dist = math.sqrt((p[0] - 0) ** 2 + (p[1] - 0) ** 2)
            heapq.heappush(kClosest, ((-1) * dist, p))
            while len(kClosest) > k:
                heapq.heappop(kClosest)
        
        ans = []
        while kClosest:
            _, point = heapq.heappop(kClosest)
            ans.append(point)
        
        return ans
        