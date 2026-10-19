class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sFreq = {}
        tFreq = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            sFreq[s[i]] = 1 + sFreq.get(s[i], 0)
            tFreq[t[i]] = 1 + tFreq.get(t[i], 0)
        sList = set(sFreq.values())
        tList = set(tFreq.values())
        return sList == tList