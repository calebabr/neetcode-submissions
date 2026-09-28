class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        best = 0
        lIdx = {}
        for r in range(len(s)):
            if s[r] in lIdx and lIdx[s[r]] >= l:
                l = lIdx[s[r]] + 1
            lIdx[s[r]] = r
            best = max(best, r - l + 1)
        return best