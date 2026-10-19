class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        i = 0
        patternMap = {}
        for char in pattern:
            subWord = ''
            while i < len(s):
                if s[i] == ' ':
                    i += 1
                    break
                subWord += s[i]
                i += 1
            if char in patternMap:
                if patternMap[char] != subWord:
                    return False
            else:
                patternMap[char] = subWord
        return True

            
