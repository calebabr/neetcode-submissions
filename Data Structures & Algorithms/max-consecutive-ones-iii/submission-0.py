class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k >= n:
            return n
        left = [0] * (n+1) # run of 1s starting at index i-1
        for i in range(n):
            if nums[i] == 1:
                left[i+1] = left[i] + 1 
            else: 
                left[i + 1] = 0
        
        right = [0] * (n+1) # run of 1s starting at index i
        for i in range(n-1, -1, -1):
            if nums[i] == 1:
                right[i] = right[i+1] + 1
            else:
                right[i] = 0
        
        best = 0
        for i in range(n-k+1):
            best = max(best, left[i] + k + right[i])
        
        return best