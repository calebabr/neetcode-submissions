class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in sMap and t[i] not in tMap:
                sMap[s[i]] = t[i]
                tMap[t[i]] = s[i]
            elif (s[i] in sMap and t[i] not in tMap) or (s[i] not in sMap and t[i ] in tMap):
                return False
            else:
                if sMap[s[i]] != t[i] and tMap[t[i]] != s[i]:
                    return False
        return True