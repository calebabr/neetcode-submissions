class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        i = 0
        patternMap = {}
        wordMap = {}
        numSubWords = 0
        for char in pattern:
            subWord = ''
            while i < len(s):
                if s[i] == ' ':
                    i += 1
                    numSubWords += 1
                    break
                subWord += s[i]
                i += 1
            if numSubWords > len(pattern):
                return False
            if char in patternMap:
                if patternMap[char] != subWord:
                    return False
                if wordMap[subWord] != char:
                    return False
            else:
                patternMap[char] = subWord
                wordMap[subWord] = char
        numSubWords += 1
        if numSubWords != len(pattern):
            return False
        return True

            
