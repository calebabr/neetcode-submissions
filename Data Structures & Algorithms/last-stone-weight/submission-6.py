class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            if s1 == s2:
                continue
            elif s2 > s1: # s2 = -5, s1 = -10
                heapq.heappush(stones, -(s2-s1))
            else:
                heapq.heappush(stones, -(s1 - s2))
        if len(stones) == 1:
            return (-1) * stones.pop()
        else:
            return 0
            