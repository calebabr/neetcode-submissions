class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        typeCount = {}
        bestSize = 0
        for r in range(len(fruits)):
            typeCount[fruits[r]] = 1 + typeCount.get(fruits[r], 0)
            while len(typeCount) > 2:
                typeCount[fruits[l]] -= 1
                if typeCount[fruits[l]] == 0:
                    del typeCount[fruits[l]]
                l += 1
            
            bestSize = max(bestSize, r - l + 1)
        return bestSize