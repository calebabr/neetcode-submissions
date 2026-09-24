class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        reach = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            reach[i] = min(reach[i - 1] + cost[i-1], reach[i - 2] + cost[i-2])
        return reach[len(cost)]