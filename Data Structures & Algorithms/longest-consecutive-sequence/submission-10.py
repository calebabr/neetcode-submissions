class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        l = 1
        best = 0
        for num in nums:
            numSet.add(num)
        for num in numSet:
            if not (num - 1) in numSet: # this means we are at the start of a sequence, thus start counting
                curr = num + 1
                l = 1
                while curr in numSet:
                    l += 1
                    curr += 1
                best = max(best, l)
        # print(numSet)
        return best