class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sAlpha = [0] * 26
        tAlpha = [0] * 26
        for i in s:
            iNum = ord(i) - 97
            sAlpha[iNum] += 1
        for j in t:
            jNum = ord(j) - 97
            tAlpha[jNum] += 1
        return sAlpha == tAlpha