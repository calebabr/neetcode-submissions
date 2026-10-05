class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = (-1) * stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            top1 = (-1) * heapq.heappop(stones)
            top2 = (-1) * heapq.heappop(stones)

            if top1 == top2:
                continue
            elif top1 > top2:
                heapq.heappush(stones, -(top1 - top2))
            else:
                heapq.heappush(stones, -(top2-top1))
        
        if len(stones) == 1:
            return (-1) * heapq.heappop(stones)
        else:
            return 0