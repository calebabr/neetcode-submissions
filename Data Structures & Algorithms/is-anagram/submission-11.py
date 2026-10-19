class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = {}
        freqT = {}
        if (len(s) != len(t)):
            return False
        
        for i in range(len(s)):
            freqS[s[i]] == 1 + countS.get(s[i], 0)
            freqT[t[i]] == 1 + countT.get(t[i], 0)
        return (freqS == freqT)        
