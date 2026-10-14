class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def bt(i, runSum):
            # Process path. Satisfy condition exceed condition
            if runSum == target:
                res.append(path[:])
                return
            if runSum > target:
                return
            
            # Traverse path. Allow repeating elements
            for j in range(i, len(nums)):
                path.append(nums[j]) # Add this number to path
                runSum += nums[j] # Use it to calc runSum
                bt(j, runSum) # calculate this paths runSum
                path.pop() # pop and remove its contribution to runSum
                runSum -= nums[j]
        
        bt(0, 0)
        return res
                
