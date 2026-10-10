class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def backtrack(i, runSum):
            if runSum == target:
                res.append(path[:])
                return
            if runSum > target:
                return
            
            for j in range(i, len(nums)):
                path.append(nums[j])
                runSum += nums[j]
                backtrack(j, runSum)
                path.pop()
                runSum -= nums[j]
        
        backtrack(0, 0)
        return res