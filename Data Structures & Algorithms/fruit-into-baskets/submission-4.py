class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        typeCount = {}
        best = 0
        numTypes = 0
        for r in range(len(fruits)):
            if fruits[r] not in typeCount or typeCount[fruits[r]] == 0:
                numTypes += 1

            typeCount[fruits[r]] = 1 + typeCount.get(fruits[r], 0)

            while numTypes > 2:
                typeCount[fruits[l]] -= 1
                if typeCount[fruits[l]] == 0:
                    numTypes -= 1
                l += 1
            
            best = max(best, r - l + 1)

        return best