class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()
        path = []

        def backtrack():
            # Process path
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            # Traverse
            for i in range(len(nums)):
                if nums[i] not in used:
                    path.append(nums[i])
                    used.add(nums[i])
                    backtrack()
                    path.pop()
                    used.remove(nums[i])
        
        backtrack()
        return res