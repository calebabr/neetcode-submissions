class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1i = 0
        w2i = 0
        mergLen = len(word1) + len(word2)
        merged = ""
        for i in range(mergLen):
            if w1i < len(word1):
                merged += word1[w1i]
                w1i += 1
            if w2i < len(word2):
                merged += word2[w2i]
                w2i += 1
        return merged

        