class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()
        path = []

        def backtrack():
            # Process path
            if len(path) == len(nums): # permutations of nums but order doesnt matter
                res.append(path[:])
                return
            
            # Traverse and add if we havent used the number
            for i in range(len(nums)):
                if nums[i] not in used:
                    path.append(nums[i])
                    used.add(nums[i])
                    backtrack()
                    path.pop()
                    used.remove(nums[i])
        
        backtrack()
        return res