class Solution:
    def firstUniqChar(self, s: str) -> int:
        i = 0
        charSet = defaultdict(list)
        while i < len(s):
            if s[i] not in charSet:
                charSet[s[i]] = [i, 1]
            else:
                charSet[s[i]][1] += 1
            i += 1
        for char in charSet:
            if charSet[char][1] == 1:
                return charSet[char][0]
        return -1