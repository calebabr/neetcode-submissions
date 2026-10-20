class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def bt(i):
            # path is already a subset, append
            res.append(path[:])

            # no duplicates, start path from i + 1
            for j in range(i, len(nums)):
                path.append(nums[j])
                bt(j + 1)
                path.pop()
        
        bt(0)
        return res