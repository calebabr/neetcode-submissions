class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        l = 1
        best = 0
        for num in nums:
            if num not in numSet:
                numSet.add(num)
        for num in numSet:
            if (num - 1) not in numSet: # we are at the start of a sequence
                l = 1
                curr = num + 1
                while curr in numSet:
                    curr += 1
                    l += 1
                best = max(l, best)
        return best
                