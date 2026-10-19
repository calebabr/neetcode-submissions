class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charMap = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in charMap:
                charMap[s[i]] = t[i]
            else:
                if charMap[s[i]] != t[i]:
                    return False
        return True