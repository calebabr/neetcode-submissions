class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransDict = {}
        magDict = {}
        for i in range(len(ransomNote)):
            if ransomNote[i] not in ransDict:
                ransDict[ransomNote[i]] = 0
            ransDict[ransomNote[i]] += 1
        for i in range(len(magazine)):
            if magazine[i] not in magDict:
                magDict[magazine[i]] = 0
            magDict[magazine[i]] += 1

        # print(magDict)
        # print(ransDict)
        
        for char in ransDict:
            if char not in magDict or ransDict[char] > magDict[char]:
                return False
        return True