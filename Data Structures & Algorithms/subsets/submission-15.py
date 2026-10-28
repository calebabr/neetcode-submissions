class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def bt(i):
            # Process path
            # Any collection (nonempty + empty) of values is a valid subset
            res.append(path[:])

            # Traverse path
            for j in range(i, len(nums)):
                path.append(nums[j])
                bt(j+1)
                path.pop()
        bt(0)
        
        return res