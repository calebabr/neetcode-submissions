class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        firstLetter = 0
        foundLetter = False
        for i in range(len(s)-1, -1, -1):
            if foundLetter:
                firstLetter = i
                foundLetter = True
            if s[i] == ' ' and foundLetter:
                return firstLetter - i + 1
        return firstLetter + 1