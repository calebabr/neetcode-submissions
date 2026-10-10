class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(i):
            # if len(path) == i:
            res.append(path[:])
            
            for j in range(i, len(nums)):
                path.append(nums[j])
                backtrack(j + 1)
                path.pop()
        
        backtrack(0)
        return res