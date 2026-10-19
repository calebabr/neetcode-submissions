class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(i):
            if i == len(nums):
                res.append(path[:])
            
            for j in range(i, len(nums)):
                path.append(nums[i])
                backtrack(j + 1)
                path.pop()
        backtrack(0)
        return res