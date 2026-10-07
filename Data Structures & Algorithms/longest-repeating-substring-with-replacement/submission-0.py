class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqDict = {}
        maxCount = 0
        l = 0
        r = 0
        best = 0
        while r < len(s):
            freqDict[s[r]] = 1 + freqDict.get(s[r], 0)
            maxCount = max(maxCount, freqDict[s[r]])
            while (r - l + 1) - maxCount > k:
                freqDict[s[l]] -= 1
                l += 1
            best = max(best, r-l+1)
            r += 1
        return best