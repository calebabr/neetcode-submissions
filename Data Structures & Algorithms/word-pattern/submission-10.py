class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordMap = {}
        patternMap = {}
        # i = 0
        word = s.split()
        if len(pattern) != len(word):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in patternMap and word[i] not in wordMap:
                patternMap[pattern[i]] = word[i]
                wordMap[word[i]] = pattern[i]
            if pattern[i] in patternMap and word[i] in wordMap:
                if patternMap[pattern[i]] == word[i] and wordMap[word[i]] == pattern[i]:
                   continue
                else:
                    return False
            if pattern[i] in patternMap and word[i] not in wordMap:
                return False
            if word[i] in wordMap and pattern[i] not in patternMap:
                return False
        return True
                        