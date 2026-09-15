class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        c = [-1] * (n+1)
        c[1] = 1
        c[2] = 2
        for i in range(3, n+1):
            c[i] = c[i-1] + c[i-2]
        return c[n]