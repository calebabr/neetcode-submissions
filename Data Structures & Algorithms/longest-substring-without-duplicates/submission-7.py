class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        best = 0
        lIdx = {} # Last index occurrence
        for r in range(len(s)):
            if s[r] in lIdx and lIdx[s[r]] >= l: # if the character already exists/has been recorded and its greater than the left end, then we need to shrink window by moving left end.
                l = lIdx[s[r]] + 1
            lIdx[s[r]] = r
            best = max(best, r - l + 1)
        return best