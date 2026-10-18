class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Im given a list of piles and the number of bananas in each pile. I am also given a time h representing max time to eat all bananas. Im asked to find minimum int k such that I can eat all bananas in all piles under h hours. Since I need to find min int k, the search space will be possible values of k. I can either eat 1 banana per hour or eat the max of piles per hour. 
        # For each possible k in search space, calc the total time itd take to eat all piles. If total time <= h, we keep this time but make search space smaller by moving r smaller. If total time is too long, we increase l to find higher possible values. Once l <= r, return the best recorded time
        l, r = 1, max(piles)
        res = 0
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(float(p) / k)
            if hours <= h:
                res = k
                r = k-1
            else:
                l = k + 1
        return res