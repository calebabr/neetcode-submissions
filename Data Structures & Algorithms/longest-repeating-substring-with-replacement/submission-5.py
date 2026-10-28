class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqDict = {}
        maxCount = 0
        best = 0
        l = 0
        for r in range(len(s)):
            freqDict[s[r]] = 1 + freqDict.get(s[r], 0)
            maxCount = max(maxCount, freqDict[s[r]])
            currSize = r - l + 1
            while (currSize - maxCount > k):
                freqDict[s[l]] -= 1
                l += 1
                currSize = r - l + 1
            best = max(best, r-l+1)
        return best
            