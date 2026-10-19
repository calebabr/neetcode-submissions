class Solution:
    def firstUniqChar(self, s: str) -> int:
        i = 0
        charSet = {}
        while i < len(s):
            if s[i] not in charSet:
                charSet[i] = 1
            else:
                charSet[i] += 1
            i += 1
        for idx in charSet:
            if charSet[idx] == 1:
                return charSet[idx]
        return -1