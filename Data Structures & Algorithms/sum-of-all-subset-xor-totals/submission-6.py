class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0 # running total
        path = [] # each traversal path

        def backtrack(i):
            nonlocal total
            x = nums[i]
            # for num in path:
                # x ^= num # get the xor sum of this traversal path
            total ^= x # add path xor sum to total
            for j in range(i, len(nums)): # increase path, backtrack, pop
                path.append(nums[j])
                backtrack(j + 1)
                path.pop()

        backtrack(0)
        return total