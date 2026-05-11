class Solution:
    def climbStairs(self, n: int) -> int:
        # Either make a step of 1 or step of 2
        # We know two options (step 1 or 2)
        # Steps to get to ith step means either take 1 step from step i-1
        # or 2 steps from i-2
        # == Steps to get to ith step is sum of possibilities from 
        # i-1 and i-2
        if n <= 2: # Base cases (1 and 2)
            return n
        count = [-1] * (n + 1)
        count[1] = 1
        count[2] = 2
        # Define step i based on i-1 or i-2
        for i in range (3, n + 1):
            count[i] = count[i-1] + count[i-2]
        return count[n]

        
        