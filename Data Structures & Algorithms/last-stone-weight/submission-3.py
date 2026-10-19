class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1 = stones.pop()
            s2 = stones.pop()
            if s1 == s2:
                continue
            elif (-1) * s2 > (-1) * s1:
                heapq.heappush(stones, -(s1-s2))
            else:
                heapq.heappush(stones, -(s2-s1))
        if len(stones) == 1:
            return -stones.pop()
        else:
            return 0
            