class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # res = []
        def backtrack(i, xorr):
            total = xorr
            for j in range(i, len(nums)):
                total += backtrack(j + 1, xorr ^ nums[j])
            return total
        # print(res)
        return backtrack(0, 0)
