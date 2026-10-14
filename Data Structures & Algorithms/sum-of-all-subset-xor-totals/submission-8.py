class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0 # running total
        path = [] # each traversal path

        def backtrack(i):

            # Process path
            nonlocal total
            x = 0
            for num in path:
                x ^= num # get the xor sum of this traversal path
            total += x # add path xor sum to total

            # Traverse path
            for j in range(i, len(nums)): # increase path, backtrack, pop
                path.append(nums[j])
                backtrack(j + 1)
                path.pop()

        backtrack(0)
        return total