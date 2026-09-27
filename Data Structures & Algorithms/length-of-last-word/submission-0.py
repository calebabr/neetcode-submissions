class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        firstLetter = 0
        foundFirst = False
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " " and not foundFirst:
                firstLetter = i
                foundFirst = True
            if s[i] == " " and foundFirst:
                return len(s[i+1:firstLetter+1])
        return len(s[:firstLetter + 1])