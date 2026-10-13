class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0
        while l <= r:
            totalTime = 0
            k = (l + r) // 2
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h: # If total time is less than h, we save this value but keep going to see if we can do better
                res = k
                r = k - 1
            else: # total time is too big, shrink the space to bigger values for a faster time
                l = k + 1
        return res