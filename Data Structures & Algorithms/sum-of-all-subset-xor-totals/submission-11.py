class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0 # running total

        def backtrack(i, runSum):

            # Each call is a subset. add the subsets runSum to total
            nonlocal total
            total += runSum

            # Traverse path. Only pick later indices so each subset is built in index order
            for j in range(i, len(nums)): # pass new XOR as argument. no keeping track of path so no append then pop
                backtrack(j + 1, runSum ^ nums[j])

        backtrack(0, 0)
        return total