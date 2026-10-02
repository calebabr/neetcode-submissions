class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        l = 0
        bestSeq = 0
        for num in nums:
            numSet.add(num)
        for num in numSet:
            if (num - 1) not in numSet:
                l = 1
                curr = num + 1
                while curr in numSet:
                    curr += 1
                    l += 1
                bestSeq = max(l, bestSeq)
        return bestSeq