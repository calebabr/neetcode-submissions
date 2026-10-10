class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i, path):
            # Base case (we've explored all)
            if i == len(nums):
                res.append(path[:])
                return
            
            # Decision 1 Include the number at i
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

            # Decision 2 Dont include number at i
            backtrack(i + 1, path)
        
        backtrack(0, [])
        return res