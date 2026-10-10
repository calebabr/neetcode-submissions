class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        path = []
        def backtrack(i):
            nonlocal total
            x = 0
            for num in path:
                x ^= num
            total += x
            for j in range(i, len(nums)):
                path.append(nums[j])
                backtrack(j + 1)
                path.pop()
        backtrack(0)
        return total
