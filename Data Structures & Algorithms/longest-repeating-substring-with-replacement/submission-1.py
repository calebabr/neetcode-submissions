class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqDict = {}
        maxCount = 0
        l = 0
        r = 0
        best = 0
        # For any window size x, the number of replacements k to make every letter the same would be to choose the highest freq letter with freq f. x - f <= k  (choose up to k letters so that freq of this letter is now x. The highest freq letter requires the least amount of change). Change window size by incrementing l and decreasing its freq while x - f > k
        for r in range(len(s)):
            freqDict[s[r]] = 1 + freqDict.get(s[r], 0)
            maxCount = max(maxCount, freqDict[s[r]])
            while (r - l + 1) - maxCount > k:
                freqDict[s[l]] -= 1
                l += 1
            best = max(best, r-l+1)
        return best