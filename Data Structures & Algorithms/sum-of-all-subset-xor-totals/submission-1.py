class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
        def backtrack(i, subset):
            xorr = 0
            for num in subset:
                xorr ^= num
            res.append(xorr)
            for j in range(i, len(nums)):
                subset.append(nums[j])
                backtrack(j + 1, subset)
                subset.pop()
        backtrack(0, [])
        # print(res)
        total = 0
        for i in range(len(res)):
            total += res[i]
        return total