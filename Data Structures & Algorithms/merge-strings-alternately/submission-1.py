class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = 0
        w2 = 0
        merged = ""
        lenMerged = len(word1) + len(word2)
        for i in range(lenMerged):
            if w1 < len(word1):
                merged = merged + word1[i]
                w1 += 1
            if w2 < len(word2):
                merged = merged + word2[i]
                w2 += 1
        return merged