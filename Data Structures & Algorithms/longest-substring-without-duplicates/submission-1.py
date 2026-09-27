class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        best = 0
        lastIdx = {}

        for r in range(len(s)):
            if s[r] in lastIdx and lastIdx[s[r]] >= l:
                l = lastIdx[s[r]] + 1
            lastIdx[s[r]] = r
            best = max(best, r - l + 1)
        return best  