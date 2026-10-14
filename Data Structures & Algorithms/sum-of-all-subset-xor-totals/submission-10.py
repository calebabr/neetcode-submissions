class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0 # running total

        def backtrack(i, runSum):

            # Process latest addition to "path". add to total
            nonlocal total
            total += runSum

            # Traverse path. Only pick later indices so each subset is built in index order
            for j in range(i, len(nums)): # traverse by calling bactrack again with new runSum
                backtrack(j + 1, runSum ^ nums[j])

        backtrack(0, 0)
        return total