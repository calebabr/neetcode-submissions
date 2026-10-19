class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        best = 0
        lIdx = {}
        for r in range(1, len(s)):
            if s[r] in lIdx and l <= lIdx[s[r]]:
                l = lIdx[s[r]] + 1
            best = max(best, r - l)
        return best