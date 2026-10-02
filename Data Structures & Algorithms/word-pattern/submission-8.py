class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        i = 0
        patternMap = {}
        wordMap = {}
        word = s.split()
        if len(pattern) != len(word):
            return False
        for i in range(len(pattern)):
            print(i, " ", pattern[i], ", ", word[i])
            if pattern[i] not in patternMap and word[i] not in wordMap:
                patternMap[pattern[i]] = word[i]
                wordMap[word[i]] = pattern[i]
            if pattern[i] in patternMap and word[i] in wordMap:
                if wordMap[word[i]] == pattern[i] and patternMap[pattern[i]] == word[i]:
                    continue
                else:
                    return False
            if pattern[i] in patternMap and word[i] not in wordMap:
                return False
            if word[i] in wordMap and pattern[i] not in patternMap:
                return False
        return True

            
