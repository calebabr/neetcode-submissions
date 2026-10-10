class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()
        path = []
        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return 
            
            for j in range(len(nums)):
                if nums[j] not in used:
                    path.append(nums[j])
                    used.add(nums[j])
                    backtrack()
                    path.pop()
                    used.remove(nums[j])
        backtrack()
        return res
