class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        if (len(s) != len(t)):
            return False
        
        for i in range(len(s)): # iterate through s, O(n)
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return (countS == countT)
