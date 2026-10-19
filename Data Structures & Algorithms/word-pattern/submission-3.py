class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        i = 0
        patternMap = {}
        wordMap = {}
        for char in pattern:
            subWord = ''
            while i < len(s):
                if s[i] == ' ':
                    i += 1
                    break
                subWord += s[i]
                i += 1
            if char in patternMap and subWord in wordMap:
                if patternMap[char] != subWord or wordMap[subWord] != char:
                    return False
            else:
                patternMap[char] = subWord
                wordMap[subWord] = char
        print(patternMap)
        return True

            
